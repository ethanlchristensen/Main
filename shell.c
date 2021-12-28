/* AUTH: Ethan Christensen
 * DATE: 11-24-21 (DUE: 112-12-21)
 * COURSE: CSCI: 4500 (SEC: 002)
 * PROJECT: #1
 * DESC: Implement Preprojects and knowledge or operating systems
 *       to write a simple shell program to proccess user inputted
 *       commands
*/
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<signal.h>
#include<sys/errno.h>
#include<sys/types.h>
#include<sys/wait.h>

#define MAX_TOKEN 10
#define MAX_CMDLINE_SIZE 200
#define MAX_JOBS_PER_LINE 100
#define MAX_PATH_SIZE 50
#define MAX_SEQOPS 100
#define MAX_SIMPLE_CMDS 100
#define MAX_ARGS_PER_CMD 100
#define BUF_SIZE 256

/* Global variables . . . */
char cmdline[MAX_CMDLINE_SIZE];
char *jobs[MAX_JOBS_PER_LINE];
char *paths[MAX_PATH_SIZE];
int seqops[MAX_SEQOPS];
char *simple_cmds[MAX_SIMPLE_CMDS];
char *cmd;
char *cmdargs[MAX_ARGS_PER_CMD];
char *path = NULL;
extern char **environ;

/* Prototypes . . . */
void show_prompt( char *prompt);

int split_into_jobs( char *cmdline, char *jobs[], size_t count );

int scan_seqops( int seqops[], char *jobstr, size_t count );

int extract_simple_cmds( char *simple_cmd, char *cmdargs[], size_t count );

int extract_cmd_args( char *simple_cmd, char **cmd, char *cmdargs[], size_t count );

int readline( int fd, char *buf, int bufsz );

int writeline( int fd, const char *str );

int split_into_paths( char *path, char *paths[], size_t count );

/* Fucntions */
int writeline( int fd, const char *str ) {
	int i;
	const size_t MAXSTRLEN = 256;
	for( i = 0; i < MAXSTRLEN; i++ ) {
		if( str[i] == '\0' ) {
			write( fd, "\n", 1 );
			break;
		} else {
			write( fd, &str[i], 1 );
		}
	}
	return i + 1; /* return number of char written */
}

int readline ( int fd, char *buf, int bufsz ) {
        int i;
        int rval;
        for( i = 0; i < bufsz - 1; i++ ) {
                rval = read( fd, &buf[i], 1 );
                if ( rval == 1) {
                        if( buf[i] == '\n') {
                                buf[i] = '\0';
                                return i + 1;
                        } else if (buf[i] == '\0') {
                                buf[i] = '\n';
                        }
                } else if ( rval == 0 ) {
                        return i;
                }
        }
        return i + 1;
}

// show_prompt will print the prompt and flush stdout
void show_prompt ( char *prompt ) {
    printf( "%s", prompt );
    fflush( stdout );
}

/* This splits that path string into seperate paths. */
int split_into_paths( char *path, char *paths[], size_t count ) {
    int i;
    char *token;
    for ( i = 0, token = strtok( path, ":"); token != NULL && i < count; token = strtok( NULL, ":" ), ++i ) {
        paths[i] = token;
    }
    return i;
}

// takes in a cmdline string and splits the line at ";"
// return: number of jobs
int split_into_jobs ( char *cmdline, char *jobs[], size_t count ) {
    int i;
    char *token;
    for ( i = 0, token = strtok( cmdline, ";" ); token != NULL && i < count; token = strtok( NULL, ";" ), ++i ) {
        jobs[i] = token; // stored into global jobs array
    }
    return i; // numbers of jobs
}

// given a job it will search for "&&" and  "||" and mark them into
// the seqops array where 1 -> "&&" and 2 -> "||"
// return: number of seqops in the job
int scan_seqops ( int seqops[], char *jobstr, size_t count ) {
    int i, sq;
    i = 0; // = position in job string
    sq = 0; // = number of seqops found
    while ( jobstr[i] != '\0') { // looping through the job to find all "&&" and "||"
        if ( jobstr[i] == '|' ){
            seqops[sq] = 2;
            sq++;
            i+=2; // skip over the second '|'
        } else if ( jobstr[i] == '&' ) {
            seqops[sq] = 1;
            sq++;
            i+=2; // skip over the second '&'
        } else {
            i++;
        }
    }
    return sq;
}

// now that we know where the seqops happen we can tokenize it and remove the "||" and  "&&" without worry
// split the job down into simple groups of commands that were seperated by "||" and "&&"
// return: number of commands delimited by "||" and "&&"
int extract_simple_cmds ( char *jobstr, char *simple_cmds[], size_t count ) {
    int i;
    char *token;
    for ( i = 0, token = strtok( jobstr, "|&" ); token != NULL && i < count; token = strtok( NULL, "|&" ), ++i ) {
        simple_cmds[i] = token; 
    }
    return i;
}


// given a simple command, the first word is the command and anything that follows is an argument
// return: number of tokens -> cmd + total args
int extract_cmd_args( char *simple_cmd, char **cmd, char *cmdargs[], size_t count ) {
    int i;
    char *token;
    for ( i = 0, token = strtok( simple_cmd, " " ); token != NULL && i < count; token = strtok( NULL, " " ), ++i ) {
        if ( i == 0 ) {
            *cmd = token;
        } else {
            cmdargs[ i - 1 ] = token; // need to offset i because i already incremented once for the first word
        }
    }
    return i;
}

int main(void) {
    // Declare variables used in main and print opening message
    int bytes_read, total_jobs, total_paths, seqops_cnt, total_simple_cmds, total_tokens, i, sn, j, k, t, index, child_status;
    char *delim, check_path[200];
    pid_t pid, which_child;

    path = getenv( "PATH" );
    if( path == NULL ) {
        fprintf( stderr, "ERROR: getenv() failed.\n");
        exit( EXIT_FAILURE );
    } else {
        total_paths = split_into_paths( path, paths, MAX_PATH_SIZE );
        printf( "total_paths: %d\n", total_paths );
    }

    printf( "*** Batchline Parser v0.1 ***\n\n" );
    while(1) {
        show_prompt( ">> ");

        printf( "Begin by entering a complete line and hitting [Enter]:\n" ); // prompt to input

        show_prompt( ">> " ); // prompt so signify program and not UNIX prompt

        bytes_read = readline( 0, cmdline, MAX_CMDLINE_SIZE ); // read the line

        printf( "\n" );

        if ( bytes_read > 0 ) { // if not EOF run main section

            //printf( "readline(): Got: \"%s\" (rval = %d)\n\n", cmdline, bytes_read); // print what was read

            total_jobs = split_into_jobs ( cmdline, jobs, MAX_JOBS_PER_LINE ); // split the string into jobs

            for ( i = 0; i < total_jobs; ++i ) {

                //printf( "Job #%d: \"%s\"\n", i, jobs[i] ); // printing the current job

                seqops_cnt = scan_seqops( seqops, jobs[i], MAX_SEQOPS ); // getting and printing the seqops for the job

                //printf( "\tseqops[] = [ "); // printing contents of the current state of seqops array

                /* for ( sn = 0; sn < seqops_cnt; sn++ ) {

                    printf( "%d ", seqops[sn] );

                }
                printf( "]\n" ); */

                total_simple_cmds = extract_simple_cmds( jobs[i], simple_cmds, MAX_SEQOPS ); // getting each command delimited by the seqops

                for ( j = 0; j < total_simple_cmds; ++j ) {

                    //printf( "\tSimple Command #%d = \"%s\"\n", j, simple_cmds[j] ); // printing the simple command

                    total_tokens = extract_cmd_args( simple_cmds[j], &cmd, cmdargs, MAX_ARGS_PER_CMD ); // breaking up the command

                    for ( k = 0; k < total_paths; ++k ) {

                        sprintf( check_path, "%s/%s", paths[k], &cmd[0] );

                        if( access( check_path, X_OK ) == 0 ) {

                            pid = fork();

                            if ( pid == -1 ) {

                                fprintf( stderr, "ERROR: calling fork().\n" );

                                exit( EXIT_FAILURE );

                            }

                            /* CHILD RUNNING THE COMMAND WHILE PARENT WAITS */
                            if( pid == 0 ) { 
            
                                if ( total_tokens == 1 ) { // if only a cmd then no args

                                    //printf( "\t\tpath:\t\t%s\n", check_path );

                                    //printf( "\t\tcmd:\t\t\"%s\"\n", &cmd[0] ); // print lone command

                                    //printf( "\t\targs:\t\t(None supplied)\n"); // print no args
                                    
                                    cmdargs[0] = check_path;

                                    if( execve( check_path, cmdargs, environ ) < 0 ) {

                                        fprintf( stderr, "ERROR: execve().\n" );

                                        exit( EXIT_FAILURE );

                                    }

                                } else {

                                    //printf( "\t\tpath:\t\t%s\n", check_path );

                                    /*for ( t = 0; t < total_tokens; ++t ) { // print the command and args

                                        if ( t == 0 ) {

                                            printf( "\t\tcmd:\t\t\"%s\"\n", &cmd[0] ); //print lone command

                                        } else {

                                            printf( "\t\targ[%d]:\t\t\"%s\"\n", t - 1, cmdargs[t - 1] ); // print args

                                        }
                                    } */

                                    if( execve( check_path, cmdargs, environ ) < 0 ) {

                                        fprintf( stderr, "ERROR: execve().\n" );

                                        exit( EXIT_FAILURE );

                                    }
                                }
                            }

                            else if( pid > 0 ) {

                                which_child = wait ( &child_status );

                                if( which_child == -1 ) {

                                    fprintf( stderr, "ERROR: wait() failed.\n" );

                                    exit( EXIT_FAILURE );

                                }
                            }

                            memset( check_path, 0, 200 );

                            memset( cmdargs, 0, 100 );

                            break;
                        }

                        if ( k == total_paths - 1 ) {
                            show_prompt( ">> " );
                            fprintf( stderr, "ERROR: %s command not found.\n", &cmd[0] );

                        }                      
                    }
                }

                printf( "\n" );

            }
        } else {

            show_prompt( ">> " );

            printf( "readline(): Returned with code = %d\n", bytes_read ); // readline gets EOF

            show_prompt( ">> Exiting . . .\n" ); // print exiting prompt

            exit( EXIT_SUCCESS ); // exit program

        }
    }
}
