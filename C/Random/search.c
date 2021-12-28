#include <stdio.h> 
#include <stdlib.h> 
 
int main(int argc, char * argv[]) 
{ 
	// This program reads a file from its arguments and prints a word by word. Additionally, it counts the words in the file. 
	if (argc < 2) return 1; 
	char * filename = argv[1]; 
	FILE * fp = fopen(filename, "r"); 
	if (fp == NULL) return 1; 
	char c; 
	int count = 0; 
    int wordsize = 0;
    int curlinesize = 0;
    char *out;
    char *word;
    int i = 0;
    int j = 0;
    if ( fp == NULL ) {
        printf("could not open file");
    }
	while((c = fgetc(fp)) != EOF) 
	{ 
		if(c == ' ' || c == '\n') 
		{  
            printf("%s\n", word);
			++count;
            j += i;
            if (j < 60) {
                printf("WORD ADDED\n");

            } else {
                printf("%s", out);
                out = "";
                out = out + *word;
                j = 0;
            }
            i = 0;
            wordsize = 0;
		} 
		else 
		{  
            word[i] = c;
            i++;
            wordsize++;
		} 
	} 
	fclose(fp); 
 
	printf("This file has %d words in it.", count); 
	return 0; 
} 