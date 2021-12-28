/*
 * Auth: Ethan Christensen
 * Date: 09-20-2021 (Due: 10-03-2021)
 * Course: CSCI-4500 (Sec: 002)
 * Desc: Become familiar with read() func in c
 */

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include "csci4500utils.h"

int readline( int fd, char *buf, int bufsz );

int readline ( int fd, char *buf, int bufsz ) {
	int i;
	int rval;
	for( i = 0; i < bufsz - 1; i++ ) {
		rval = read( fd, &buf[i], 1 );
		if ( rval == 1) {
			if( buf[i] == '\n') {
				buf[i] = '\0';
				return i;
			} else if (buf[i] == '\0') {
				buf[i] = '\n';
			}
		} else if ( rval == 0 ) {
			return i;
		} 
	}
	return i + 1;
}
