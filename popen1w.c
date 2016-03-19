// This program is to read the output of process.

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#define BUFSIZE 5024


int main (int argc, char *argv[])
{

// Declare the variables that we are going to require.

FILE *write_fp;
//int result;
char buffer[BUFSIZE+1];


//initialize the buffer ans store "\0"

memset(buffer,'\0',sizeof(buffer));

sprintf(buffer,"Coffee was getting cold while she was waiting for him to miss her ! And he was finishing up the drinks one after other to forgether! ");

//open the pipe in write  mode ie wite the ouput to command od -c


write_fp=popen("od -c","w");

	if(write_fp!=NULL)
	{
		fwrite(buffer,sizeof(char),BUFSIZE,write_fp);
		
		pclose(write_fp);
		exit(EXIT_SUCCESS);
	}
	else
	{
		perror("popen:");
		exit(EXIT_FAILURE);
	}



return 0;
}
