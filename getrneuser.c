#include<unistd.h>
#include<sys/types.h>
#include <stdio.h>
#include<stdlib.h>
int main (int argc, char *argv[])
{

int status;
uid_t r,e;
pid_t proc_id;
uid_t getuid(void);
uid_t getgid(void);

printf("Real User Id: %d\n\n",getuid());

printf("Effective User Id: %d\n\n",getgid());


printf("Process  Id: %d\n\n",getpid());


printf("Process Gruop Id: %d\n\n",getpgrp());

printf("process Group ID:%d\n\n",getpgid(getpid()));

proc_id=fork();

if(proc_id== -1)
{
	perror("fork:\n");
	exit(EXIT_FAILURE);

}
else if(!proc_id)
{
	printf("Hi I am a Child !!! \n\n");
	printf("CHild Process  Id: %d\n\n",getpid());


	printf("Child Process Gruop Id: %d\n\n",getpgrp());

	printf("Child process Group ID:%d\n\n",getpgid(getpid()));

	status=setpgid(getpid(),5000);
	if(status == -1 )
	{
		perror("setpgid:\n\n");
		exit(EXIT_FAILURE);
	}	
	else
	{
		 printf("CHild Process  Id: %d\n\n",getpid());


        	printf("Child Process Gruop Id: %d\n\n",getpgrp());
	
	        printf("Child process Group ID:%d\n\n",getpgid(getpid()));
	}
	

}

return 0;
}
