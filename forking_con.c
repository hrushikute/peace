#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main (int argc,char * argv[])
{
	pid_t process_id_child,process_id_parent;

	pid_t ret=fork();

	if (ret==0)
	{

	printf("I am Child Process: Below are my details :\n\n");
	printf(" Parent Process ID: %d \n",getppid());


	printf(" Child Process ID: %d \n",getpid());
	}


	else
	{

	printf("I am Parent Process: Below are my details :\n\n");
	printf(" Parent Process ID: %d \n",getppid());


	printf(" Child Process ID: %d \n",getpid());

	}

return 0;
}
