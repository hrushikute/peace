#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<pthread.h>

void* thread_fun(void* arg);

char message[]="Pahila thread program !";

int main(int argc , char* argv[])
{

int result;
void* thread_result;

pthread_t TH;

result=pthread_create(&TH,NULL,thread_fun,(void*)message);
if(result!=0)
{
	perror("pthread_create:");
	exit(EXIT_FAILURE);
	
}

printf("Waiting for thread TH to finish.\n ");

result=pthread_join(TH,&thread_result);

if(result!=0)
{
	perror("pthread_join:");
	exit(EXIT_FAILURE);

}

printf("THread has joined sucessfully with stuatus: %s\n",(char *)thread_result);
printf("Message is Now: %s\n",message);
exit(EXIT_SUCCESS);


return 0;

}



void * thread_fun(void* arg)
{

printf("Executing thread : Argument was %s\n",(char * )arg);
sleep(2);
strcpy(arg,"Bye!");
pthread_exit("Thanks for the cpu time !");

}
