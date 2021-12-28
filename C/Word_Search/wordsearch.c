#include <ctype.h>
#include <stdio.h>
#include <string.h>

int search(char in[50][50], char *string, int length, int x, int y, int n);
int direction(char in[50][50], char *string, int length, int x, int y, int move_x, int move_y, int n);

char out[50][50];

int main(void)
{
    char board[50][50], string[100];
    int x, i, j, n, length;

    /* Filling output array with spaces */
    for (i = 0; i < 50; i++)
    {
        for (j = 0; j < 50; j++)
        {
            out[i][j] = ' ';
        }
    }

    x = 0;
    /* Using gets() to get each line of user input, x stores number of rows processed */
    while (gets(string))
    {
        length = strlen(string);

        /* Establishing the size of the array based off the first line of input */
        if (x == 0)
        {
            n = 0;
            for (i = 0; i < length; i++)
            {
                if (string[i] == '\n' || string[i] == '\0' || string[i] == EOF)
                {
                    break;
                }
                else
                {
                    n++;
                    /* inputting first line of input into board array */
                    if (i % 2 == 0)
                    {
                        board[x][i / 2] = string[i];
                    }
                }
            }
            /* Dividing n by two to account for the spaces */
            n /= 2;
            x++;
        }
        /* Getting n lines of input to construct the wordsearch array "a" */
        else if (x < n)
        {
            for (i = 0; i < length; i++)
            {
                if (i % 2 == 0)
                {
                    board[x][i / 2] = string[i];
                }
            }
            x++; /* incrementing the row */
        }
        else
        { 
            /* Once our x equals our expected number of lines, we know we are going to get words now */
            for (i = 0; i < n; i++)
            {
                for (j = 0; j < n; j++)
                {
                    /* if first char of string equals the current char in the board, lets search in each direction */
                    if (board[i][j] == string[0])
                    {
                        search(board, string, length, i, j, n);
                    }
                }
            }
        }
    }

    /* printing the output array that contains found words */
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%c ", out[i][j]);
        }
        if (i < n - 1)
        {
            printf("\n");
        }
    }

    return 0;
}

int search(char in[50][50], char *string, int length, int x, int y, int n)
{
    direction(in, string, length, x, y, 1, 0, n); /* searching down vertically */
   
    direction(in, string, length, x, y, -1, 0, n); /* searching up vertically */
 
    direction(in, string, length, x, y, 1, 1, n); /* searching diagonally down and to the right */
  
    direction(in, string, length, x, y, -1, 1, n); /* searching diagonally up and to the right */
    
    direction(in, string, length, x, y, 0, 1, n); /* searching horizontally to the right */
   
    direction(in, string, length, x, y, 0, -1, n); /* searching horizontally to the left */
    
    direction(in, string, length, x, y, -1, -1, n); /* searching diagonally up and to the left */
 
    direction(in, string, length, x, y, 1, -1, n); /* searching diagonally down and to the left */

    return 0;
}

int direction(char in[50][50], char *string, int length, int x, int y, int move_x, int move_y, int n)
{
    int i;
    for (i = 1; i < length; i++)
    {
        /* change what character we will look at next based on what was given in search() */
        int X = x + i * move_x;
        int Y = y + i * move_y;
        if (X < 0 || X >= n || Y < 0 || Y >= n) /* making sure not to step out of bounds */
            return 0;
        if (in[X][Y] != string[i]) /* stop the moment a character doesn't match */
            return 0;
    }

    /* If we loop successfully then the word is in the array */
    /* So we add it to the output array */
    for (i = 0; i < length; i++)
    {
        int X = x + i * move_x;
        int Y = y + i * move_y;
        out[X][Y] = in[X][Y];
    }
    return 0;
}