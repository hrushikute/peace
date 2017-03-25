#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<error.h>
#include<string.h>

#include<sys/msg.h>


#include"message.h"

int main (int argc,char * argv[])
{

int running = 1;
int msgid;
struct my_msg_st some_data;

long int msg_to_receive =0;

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
	// receive the messages sent by other process.
		if(msgrcv(msgid,(void*)&some_data,BUFSIZ,msg_to_receive,0)==-1)
		{
			fprintf(stderr,"msgrcv failed\n");
			exit(EXIT_FAILURE);
		}
		

		printf("You worote : %s",some_data.some_text);
		if(strncmp(some_data.some_text,"end",3))
		{
			running=0;
		}
	}

// delete the message Queue
if(msgctl(msgid,IPC_RMID,0)==-1)
	{
		fprintf(stderr,"msgctl failed:\n");
		exit(EXIT_FAILURE);
	}

return 0;
}
