/*
 * Auth: Ethan Christensen
 * Date: 04 - 14 - 21
 * Programming Assignment
 * Decription: This program is meant to act as the server,
 * waiting and listening for requests from the client server,
 * accepting and reading/writing files from the client server
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <arpa/inet.h>
#define BUF_SIZE (100*1024*1024)

char *in_buf = NULL;
int sockfd, cl_sockfd, bytes_read, bytes_written, fd_out, file_cntr = 1, val = 1;
struct sockaddr_in sa, cl_sa;
struct in_addr ia;
void cleanup(void);
void SIGINT_handler( int sig );

void cleanup(void) { /*closing sockets and memory*/
    if( in_buf != NULL ) {
        free( in_buf );
        in_buf = NULL;
    }
    if( cl_sockfd ) {
	close ( cl_sockfd );
	sockfd = 0;
    }
    if( sockfd ) {
	close ( sockfd );
	sockfd = 0;
    }
    if ( fd_out != 0 ) {
	close ( fd_out );
	fd_out = 0;
    }
}

void SIGINT_handler( int sig ) {
    fprintf( stderr, "\nserver: Server interrupted. Shutting down.\n" );
    cleanup();
    exit( EXIT_FAILURE );
}

int main( int argc, char *argv[] ) {
    socklen_t cl_sa_size = sizeof( cl_sa ); /* creating associated clients members */
    const char *my_ip = "127.0.0.1";
    const char *port_str = argv[1];
    char fname[80];
    unsigned short int port = (unsigned short int) atoi( port_str );
    in_buf = ( char * ) malloc( BUF_SIZE );
    signal( SIGINT, SIGINT_handler );

    if( argc <= 1 ) {
	    fprintf( stderr, "server: USAGE: server <Port>\n\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    if( port <= 1023 || port > 65535) { /* must be a valid port */
        fprintf( stderr, "server: USAGE: Port number must be 1024 - 65535.\n\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    ia.s_addr = inet_addr( my_ip ); /* assigning members in the structure */
    sa.sin_family = AF_INET;
    sa.sin_addr = ia;
    sa.sin_port = htons ( port );

    sockfd = socket( AF_INET, SOCK_STREAM, 0 ); /* creating a new socket for listening */
    if( setsockopt( sockfd, SOL_SOCKET, SO_REUSEADDR, (const void *) &val, sizeof(int) ) != 0 ) {
	fprintf( stderr, "server: ERROR: setsockopt() failed.\n\n" );
    }
    if ( sockfd < 0 ) {
        fprintf( stderr, "server: ERROR: Unable to obtain a new socket.\n\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    if ( bind( sockfd, (struct sockaddr *) &sa, sizeof(sa) ) != 0 ) { /* binding the listening socket */
        fprintf( stderr, "server: ERROR: Socket binding failed.\n\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    if ( listen( sockfd, 32 ) != 0 ) { /* listening for a client */
        fprintf( stderr, "server: ERROR: Could not turn socket into a 'listening' socket.\n\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    memset( (void*) &cl_sa, 0, sizeof( cl_sa ) );

    while(1) { /* always waiting for a client to connect to the server */
        printf( "server: Awaiting TCP connections over port %s. . .\n", argv[1] );
        cl_sockfd = accept( sockfd, (struct sockaddr *) &cl_sa, &cl_sa_size );
        if ( cl_sockfd > 0 ) {
            printf( "server: Connection accepted. . . \n" );

            bytes_read = recv( cl_sockfd, (void *) in_buf, BUF_SIZE, MSG_WAITALL ); /* read the clients buffer to the server buffer */
            if( bytes_read < 0 ) {
                fprintf( stderr, "server: ERROR: Unable to read from socket.\n\n" );
                cleanup();
                exit( EXIT_FAILURE );
            } else {
                printf( "server: Receiving file. . .\n");
            }

	        if( cl_sockfd ) { /* no longer need, close connection */
		        close ( cl_sockfd );
		        printf( "server: Connection closed.\n");
		        cl_sockfd = 0;
	        }

            sprintf( fname, "file-%02d.dat", file_cntr ); /* creating the file name per the naming scheme */
            printf( "server: Saving file: %s\n", fname );
            fd_out = open( fname, O_CREAT|O_WRONLY|O_TRUNC, S_IRUSR|S_IWUSR ); /* open file to write to */
            if (fd_out < 0 ) {
                fprintf( stderr, "server: ERROR: Could not create: %s\n\n", fname );
                cleanup();
                exit( EXIT_FAILURE );
            }

            bytes_written = write( fd_out, in_buf, (size_t) bytes_read ); /* write to the file */
            if( bytes_written != bytes_read ) {
                fprintf( stderr, "server: ERROR: Error writing ALL bytes\n\n" );
                cleanup();
                exit( EXIT_FAILURE );
            }
            printf( "server: Done.\n\n" );
            close( fd_out );
	        file_cntr++;
        } else {
            fprintf( stderr, "server: ERROR: Connection request/accept attempt failed.\n\n" );
        }
    }
    cleanup();
}