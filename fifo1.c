/* The program to create a named pipe using mkfifo */

#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>


int main(int argc, char *argv[])
{

int result;

result=mkfifo("/tmp/fifa",0777);

if(result==-1)
	{
		perror("mkfifo:");
		exit(EXIT_FAILURE);
	}
else
{

	printf("Pipe Successfully created ! \n");
	exit(EXIT_SUCCESS);
}




return 0;
}

