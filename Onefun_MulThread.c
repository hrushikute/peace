#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<pthread.h>

void* thread_fun(void* arg);

//char message[]="Pahila thread program !";

int counter=1;

int main(int argc , char* argv[])
{

int result,seq=0;
void* thread_result;

pthread_t TH1,TH2;

result=pthread_create(&TH1,NULL,thread_fun,&counter);
if(result!=0)
{
	perror("pthread_create:TH1");
	exit(EXIT_FAILURE);
	
}
printf ("created thread thread TH1 :with counter : %d ",counter);
sleep (5);
result=pthread_create(&TH2,NULL,thread_fun,&counter);
if(result!=0)
{
        perror("pthread_create TH2:");
        exit(EXIT_FAILURE);

}


printf ("created thread thread TH2 :with counter : %d ",counter);

result=pthread_join(TH1,&thread_result);
result=pthread_join(TH2,&thread_result);

if(result!=0)
{
	perror("pthread_join:");
	exit(EXIT_FAILURE);

}

printf("THread has joined sucessfully with stuatus: %s\n",(char *)thread_result);
printf("COunter is Now: %d\n",counter);
exit(EXIT_SUCCESS);


return 0;

}



void * thread_fun(void *arg)
{

printf("Executing thread : Argument was %d\n",*(int *)arg);
if(*(int *)arg==1)
	*(int *) arg=2;
else
	*(int *)arg=1;

sleep (5);
pthread_exit("Thanks for the cpu time !");

}
