#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char puzzle_out[50][50];
int direction(char puzzle[50][50], int size, int length, char word[50], int x, int y, int change_x, int change_y);
int search(char puzzle[50][50], int size, int length, char word[50], int x, int y);
void fill_output(char puzzle[50][50], int size);

int main(void)
{
  char puzzle[50][50];
  char string[100];
  char letter;
  int x = 0;
  int y = 0;
  int n = 0;
  int i, j, length;
   for(i=0;i<50;i++){
      for(j=0;j<50;j++){
         puzzle_out[i][j] = ' ';
      }
   }
  while(fgets(string, 100, stdin))
  {
      length = strlen(string);
      if(x == 0)
      {
        for (i = 0; i < length; i++)
        {
            if ( string[i] == '\n' || string[i] == '\0' || string[i] == EOF) {
               break;
            }
            else {
               if (i % 2 == 0)
               {
                  puzzle[0][i/2] = string[i];
                  n++;
               }
            }
         }
         x++;
      }
      else if(x < n)
      {
         for (i = 0; i < length - 1; i++)
         {
               if (i % 2 == 0)
               {
                  puzzle[x][i/2] = string[i];
               }
         }
         x++;
      }
      else
      {
         for (i = 0; i < n; i++)
         {
            for (j = 0; j < n; j++)
            {
               if (puzzle[i][j] == string[0])
               {
                  search(puzzle, n, length, string, i, j);
               }
            }
         }
      }
  }
  for(i=0;i<n;i++){
     for(j=0;j<n;j++){
        printf("%c ", puzzle_out[i][j]);
     }
     printf("\n");
  }
  return 0;
}

int search(char puzzle[50][50], int size, int length, char *word, int x, int y)
{
   direction(puzzle, size, length, word, x, y, 0, 1);
   direction(puzzle, size, length, word, x, y, 0, -1);
   direction(puzzle, size, length, word, x, y, 1, 0);
   direction(puzzle, size, length, word, x, y, -1, 0);
   direction(puzzle, size, length, word, x, y, 1, 1);
   direction(puzzle, size, length, word, x, y, -1, -1);
   direction(puzzle, size, length, word, x, y, -1, 1);
   direction(puzzle, size, length, word, x, y, 1, -1);
   return 0;
}

int direction(char puzzle[50][50], int size, int length, char *word, int x, int y, int change_x, int change_y)
{
   int i;
   int newx;
   int newy;
   for (i = 1; i < length; i++)
   {
      newx = x + i * change_x;
      newy = y + i * change_y;      
      if (newx < 0 || newx > size || newy < 0 || newy > size)
      {
         return 0;
      }
      else if(puzzle[newx][newy] != word[i])
      {
         return 0;
      }
   }
   
   /*fill_output(puzzle_out, size);*/
   
   for (i = 0; i < length; i++)
   {
      newx = x + i * change_x;
      newy = y + i * change_y;
      puzzle_out[newx][newy] = word[i];
   }
   
   return 0;
}
