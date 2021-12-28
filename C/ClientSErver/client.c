/*
 * Auth: Ethan Christensen
 * Date: 04 - 14 - 21
 * Programming Assignment 
 * Description: This program will read data from user inputted files,
 * allocate the data to a buffer, send the buffer through a socket
 * to another program called server.
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

char *out_buf = NULL;
int sockfd, fd_in, bytes_read, bytes_sent, i;
struct in_addr ia;
struct sockaddr_in sa;

void cleanup(void) {
    if( out_buf != NULL ) {
        free( out_buf );
        out_buf = NULL;
    }
    if( sockfd ) {
	close( sockfd );
        sockfd = 0;
    }
     if( fd_in != 0 ) {
	close ( fd_in );
	fd_in = 0;
    }
}

void SIGINT_handler( int sig ) {
    fprintf( stderr, "client: Client interrupted. Shutting down.\n" );
    cleanup();
    exit( EXIT_FAILURE );
}

int main( int argc, char *argv[]) {
    const char *port_str = argv[2];
    unsigned short int port = (unsigned short int) atoi( port_str );
    const char *my_ip = argv[1];
    out_buf = ( char * ) malloc( BUF_SIZE );
    signal( SIGINT, SIGINT_handler );
    if( argc <= 3 ) {
        fprintf( stderr, "client: USAGE: client <IP_addr> <Port> file1 file2 . . .\n" );
        cleanup();
        exit( EXIT_FAILURE );
    }

    ia.s_addr = inet_addr( my_ip ); /* assigning members of the sa structure */
    sa.sin_family = AF_INET;
    sa.sin_addr = ia;
    sa.sin_port = htons( port );

    for(i = 3; i < argc; i++ ) { /* looping through each file to send */

        sockfd = socket( AF_INET, SOCK_STREAM, 0 ); /* creating socket */
         if( sockfd < 0 ) {
            fprintf( stderr, "client: ERROR: Unable to obtain a new socket.\n\n" );
            cleanup();
            exit( EXIT_FAILURE );
        }
	    printf( "client: Connecting to %s:%s. . .\n", argv[1], argv[2] ); /* Connecting to the server */
        if( connect ( sockfd, (struct sockaddr *) &sa, sizeof(sa) ) != 0 ) {
            fprintf( stderr, "client: ERROR: Attempting to connect with the server.\n\n" );
        } else {
            
            printf("client: Success!\n" );

            fd_in = open( argv[i], O_RDONLY ); /* opening file to read to buffer */
            if ( fd_in < 0 ) {
                fprintf( stderr, "client: ERROR: Failed to open: %s\n\n", argv[i] );
            } else {

                bytes_read = read( fd_in, out_buf, BUF_SIZE ); /* reading to buffer */
                if ( bytes_read < 0 ) {
                    fprintf( stderr, "client: ERROR: Unable to read file.\n\n");
                } else {

                    printf( "client: Sending: %s\n", argv[i] );
                    bytes_sent = send( sockfd, (const void *) out_buf, (size_t) bytes_read, 0 );
                    if( bytes_sent != bytes_read ) {
                        fprintf( stderr, "client: ERROR: Failed to send all data.\n\n" );
                    }

                    printf( "client: Done.\n\n" );
                    close ( fd_in ); /* closing file after connection is finished */
	                close ( sockfd ); /* closing socket after connection is finished */
	                fd_in = 0;
	                fd_in = 0;
                    }
            }
        }
    }
    printf( "client: All files sent.\n" );
    printf( "client: Closing connection.\n" );
    cleanup();
    return 0;
}