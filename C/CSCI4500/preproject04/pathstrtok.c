#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main( void ) {
    int i;
    char *path = NULL, *delim, *tok;
    printf("Checking \"PATH\"...\n");
    path = getenv( "PATH" );
    if( path != NULL ) {
        printf("PATH = %s\n", path);
        delim = ":";
        i = 0;
        for( tok = strtok( path, delim ); tok != NULL; tok = strtok( NULL, delim) ) {
            printf("[%d] = \"%s\"\n", i, tok);
            i++;
        }
    } else {
        printf("ERROR: getenv(): Unable to obtain \"PATH\"\n");
    }
    
    return 0;
}