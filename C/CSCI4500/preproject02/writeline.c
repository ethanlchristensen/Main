/*
 * Auth: Ethan Christensen
 * Date: 09-20-2021 (Due: 10-03-2021)
 * Course: CSCI-4500 (Sec: 002)
 * Desc: contains the created writeline function
 */

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<malloc.h>
#include "csci4500utils.h"

#define BUF_SIZE 256

int writeline( int fd, const char *str );

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
