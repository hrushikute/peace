#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<stdlib.h>



int main (int argv,char *argc[])
{

	int status;
	pid_t proc_id_cnt1,proc_id_cnt2;

	printf("\n\nCurrent process_id :%d\n\n", getpid() );
	

	proc_id_cnt1=fork();

	if(proc_id_cnt1 == -1)
		perror("\n\nFork Failure:");
	
	if (!proc_id_cnt1)
	{
		 printf("\n\nI am a child process : %d", getpid() );
	
		 status=execlp("ls","ls","-lrt",NULL);
		
		if (status == -1)
			perror("execlp error:");
	}

	else
	{
		printf("\n\nThis is parent process:%d\n\n",getpid());
		
	}
return 0;

}

