// This program is for loading the uid generator of FAF.
//
// Needs uid.dll in directory to compile
//
// i586-mingw32msvc-gcc -L. -luid uid_loader.c -o uid.exe

// Needs LIBEAY32.dll in directory to run

#include<stdio.h>


int main(int argc, const char *argv[]) {
	if(argc!=3) {
		fprintf(stderr, "need two arguments!\n");
		return 1;
	}
	printf("%s",uid(argv[1],argv[2]));
	return 0;
}

