#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main () {
    char *filename = "file.txt";
    FILE *file = fopen(filename, "r");
    if (file == NULL ) {
        printf("COULD NOT OPEN!");
    } else {
        char tmp[60];
        char buffer[100];
        char word[20];
        while(fgets(buffer, 60, file)) {
            printf("%s\n", buffer);
            int i;
            for(i = 0; i < 100; i++) {
                continue;
            }
        }
        fclose(file);
    }
    return 0;
}