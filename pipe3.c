// This program is to write the data and read the data using pipe.

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#define BUFSIZE 5024


int main (int argc, char *argv[])
{

// Declare the variables that we are going to require.

//FILE *read_fp;
int result;
int filedesc[2];
const char some_data[]="Kahi pe nigahe Kahi pe nishana";
char buffer[BUFSIZE+1];

pid_t child_pid;
//initialize the buffer ans store "\0"

memset(buffer,'\0',sizeof(buffer));

//open the pipe in read mode ie read the ouput of command "uname"

if(pipe(filedesc)==0)
{
		// invoke a new process 
		child_pid=fork();
		
		if(child_pid == -1)
		{
			perror("fork:");
			exit(EXIT_FAILURE);
		}
		
		if (!child_pid)
		{
			// Read the data from the pipe
			sprintf(buffer,"%d",filedesc[0]);
			result=execl("pipe4","pipe4",buffer, (char * )0);
			if (result==-1)
			{
				perror("execl:");
				exit(EXIT_FAILURE);
			}
		}
		else
		{	
			// Write the data onto the pipe
			result=write(filedesc[1],some_data,strlen(some_data));
			printf("process %d :Data wrote in bytes :%d\n ",getpid(),result);
		}
}

else
{
	perror("pipe:");
	exit(EXIT_FAILURE);
}

return 0;
}
