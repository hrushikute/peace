#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main (int argc,char * argv[])
{
	
	int ret_exec;
	pid_t process_id_child,process_id_parent;
	pid_t ret=fork();

	if (ret==0)
	{

	printf("I am Child Process: Below are my details :\n\n");
	printf(" Parent Process ID: %d \n",getppid());

	
	printf(" Child Process ID: %d \n",getpid());
	
	ret_exec = execl("/bin/ls","ls","-lrt",NULL);

	if(ret_exec == -1)
	{
		perror("execl error:");
	
	}
	
	}


	else
	{

	printf("I am Parent Process: Below are my details :\n\n");
	printf(" Parent Process ID: %d \n",getppid());


	printf(" Child Process ID: %d \n",getpid());

	}

return 0;
}
