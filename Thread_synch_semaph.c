#include<stdio.h>
#include<semaphore.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<pthread.h>
#define WORK_SIZE 1024
/* Function Declaration*/
void *thread_fun (void *arg);

// Global Variable
sem_t sem_bin;

char work_area[WORK_SIZE];

int main (int argc , char * argv[])
{

int result;
pthread_t TH;
void *thread_result;


result=sem_init(&sem_bin,0,0);

if (result!=0)
{
	perror("sem_init:");
	exit(EXIT_FAILURE);
}

result=pthread_create(&TH,NULL,thread_fun,NULL);

if (result!=0)
{
	perror("pthread_create:");
	exit(EXIT_FAILURE);
}


printf("Input text you wish. Enter end to terminate.\n");

while(strncmp("end",work_area,3)!=0)
{
	fgets(work_area,WORK_SIZE,stdin);
	sem_post(&sem_bin);

}

result=pthread_join(TH,&thread_result);

if (result!=0)
{
	perror("pthread_join:");
	exit(EXIT_FAILURE);
}
printf("Thread Joined successfully !\n");

sem_destroy(&sem_bin);
exit(EXIT_SUCCESS);

return 0;


}




void *thread_fun (void * arg)
{
 sem_wait(&sem_bin);
 while(strncmp("end",work_area,3)!=0)
	{
	printf("NUmmber characters entered: %d\n",(int)(strlen(work_area)-1));
	sem_wait(&sem_bin);
	}

pthread_exit(NULL);

}
