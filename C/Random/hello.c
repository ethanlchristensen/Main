#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

const char out[20] = "Hello World";

int main( void ) {
    printf("%.3s", out);
    return 0;
}
