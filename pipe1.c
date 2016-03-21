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


//initialize the buffer ans store "\0"

memset(buffer,'\0',sizeof(buffer));

//open the pipe in read mode ie read the ouput of command "uname"

if(pipe(filedesc)==0)
{
		// Write the data onto the pipe
		result=write(filedesc[1],some_data,strlen(some_data));
		printf("Data wrote in bytes :%d\n ",result);

		// Read the data from the pipe
		result=read(filedesc[0],buffer,BUFSIZE);
		printf("Data read in bytes : %d : Value: %s\n",result,buffer);
		exit(EXIT_SUCCESS);

}

else
{
	perror("pipe:");
	exit(EXIT_FAILURE);
}

return 0;
}
