#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include<sys/shm.h>
#include"shared_mem.h"

int main (int argc , char *argv[])
{
int running=1;
void *shared_memory=(void*)0;
struct shared_use_st *shared_stuff;
int shmid;

shmid=shmget((key_t)1234,sizeof(struct shared_use_st),0666|IPC_CREAT);
if(shmid==-1)
{
	perror("shmget:");
	printf("\nError in creating shared memory :\n");
	exit(EXIT_FAILURE);
}

shared_memory=shmat(shmid,(void*)0,0);
if(shared_memory==(void*)-1)
{
	perror("shmat:");
	fprintf(stderr,"shmat failed \n");
	exit(EXIT_FAILURE);
}

printf("Memmory attached at %X\n",(int)shared_memory);


shared_stuff=(struct shared_use_st*)shared_memory;

shared_stuff->written_by_you=0;
while(running)
{
	if(shared_stuff->written_by_you)
	{
		printf("You wrote: %s\n",shared_stuff->some_text);
	sleep(rand() % 4);
		if(strncmp(shared_stuff->some_text,"end",3)== 0)
		{
			running=0;
		}
	}
}

if (shmdt(shared_memory)== -1)
{
	perror("shmdt:");
	fprintf(stderr,"shmdt failed!\n");
	exit(EXIT_FAILURE);
}
if(shmctl(shmid,IPC_RMID,0)==-1)
{

	perror("shmctl:");
        fprintf(stderr,"shmctl failed!\n");
        exit(EXIT_FAILURE);

}
exit(EXIT_SUCCESS);
return 0;
}
