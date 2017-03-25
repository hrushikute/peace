// This program is to read the big dataoutput of process.

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

read_fp=popen("ps -ax","r");

	if(read_fp!=NULL)
	{
		result=fread(buffer,sizeof(char),BUFSIZE,read_fp);

		if(result>0)
		{
			while(result>0)
			{
				buffer[result-1]='\0';
				printf("Output was :\n%s\n",buffer);
				result=fread(buffer,sizeof(char),BUFSIZE,read_fp);	
				
			}
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

/*
The program uses popen with an “r” parameter in a similar fashion to popen1.c . This time, it continues
reading from the file stream until there is no more data available. Notice that, although the ps command
takes some time to execute, Linux arranges the process scheduling so that both programs run when they
can. If the reader process, if program , has no input data, it’s suspended until some becomes available. If the
writer process, ps , produces more output than can be buffered, it’s suspended until the reader has con-
sumed some of the data.
*/
