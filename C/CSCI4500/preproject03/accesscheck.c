#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>

int main ( int argc, char *argv[] ) {
    int fval, rval, wval, xval;
    if ( argc < 2 || argc > 2 ) {
        printf( "\nERROR: Usage: ./accesscheck <pathname>\n\n" );
        return 0;
    } else {
        printf( "Checking: \"%s\"...\n", argv[1]);
        fval = access( argv[1], F_OK );
        printf( "F_OK = %d\n", fval);
        if( fval < 0 ) {
            printf( "\tERROR: %s (errno = %d)\n", strerror( errno ), errno );
        }

        rval = access( argv[1], R_OK );
        printf( "R_OK = %d\n", rval);
        if( rval < 0 ) {
            printf( "\tERROR: %s (errno = %d)\n", strerror( errno ), errno );
        }

        wval = access( argv[1], W_OK );
        printf( "W_OK = %d\n", wval);
        if( wval < 0 ) {
            printf( "\tERROR: %s (errno = %d)\n", strerror( errno ), errno );
        }

        xval = access( argv[1], X_OK );
        printf( "X_OK = %d\n", xval);
        if( xval < 0 ) {
            printf( "\tERROR: %s (errno = %d)\n", strerror( errno ), errno );
        }
    }
    return 0;
}