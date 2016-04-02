#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<error.h>
#include<string.h>

#include<sys/msg.h>


#include"message.h"

int main (int argc,char * argv[])
{

int running=1;
int msgid;
struct my_msg_st some_data;

char buffer[BUFSIZ];
//long int msg_to receive =0

// create a message queue.

msgid=msgget((key_t)1234,0755|IPC_CREAT);

if(msgid==-1)
	{
		perror("msgget:");
		fprintf(stderr,"msgget failed \n");
		exit(EXIT_FAILURE);

	}


while(running)

	{
	//Get the message from user.
	printf("Enter the text that you want to send:");
	fgets(buffer,BUFSIZ,stdin);
	some_data.my_msg_type=1;
	strcpy(some_data.some_text,buffer);	


	// send the message to other process
		if(msgsnd(msgid,(void*)&some_data,BUFSIZ,0)==-1)
		{
			fprintf(stderr,"msgsnd failed\n");
			exit(EXIT_FAILURE);
		}
		

		if(strncmp(some_data.some_text,"end",3))
		{
			running=0;
		}
	}


return 0;
}
