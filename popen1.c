// This program is to read the output of process.

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#define BUFSIZE 5024


int main (int argc, char *argv[])
{

// Declare the variables that we are going to require.

FILE *read_fp;
int result;
char buffer[BUFSIZE+1];


//initialize the buffer ans store "\0"

memset(buffer,'\0',sizeof(buffer));

//open the pipe in read mode ie read the ouput of command "uname"

read_fp=popen("uname -a","r");

	if(read_fp!=NULL)
	{
		result=fread(buffer,sizeof(char),BUFSIZE,read_fp);

		if(result>0)
		{
			printf("Output was :\n%s\n",buffer);
		}
		else
		{
			perror("fread:");
		}
		pclose(read_fp);
	}
	else
	{
		perror("popen:");
		exit(EXIT_FAILURE);
	}



return 0;
}
