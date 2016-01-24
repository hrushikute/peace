#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{

	int status,ret_exec;
	pid_t proc_id;
	

	printf("Parent Process id : %d\n\n",getppid());

	printf("Child before fork Process id : %d\n\n",getpid());

	if (!fork())
	{
	
		printf("CUrrent process_id : %d",getpid());
		ret_exec = execlp("uptime","uptime",NULL);

		
        	if(ret_exec == -1)
        	{
                	perror("execl error:");
			exit(EXIT_FAILURE);
        	}
	}

	proc_id=waitpid(0,&status,WNOHANG);

	if(proc_id == -1)
	{

		perror("waitpid:");
		exit(EXIT_FAILURE);
	}

	else
	{
	
		printf("Chid process Pid :%d\n",proc_id);

		if (WIFEXITED(status))
			printf(	"Normal termination of process with status %d \n\n",WIFEXITED(status));

		if(WIFSIGNALED(status))
			printf("Process was killed bu signal %d : %s \n\n\n",WTERMSIG(status),WCOREDUMP(status)?"dump core":"");

		if (WIFSTOPPED(status))
			printf("Stopped by Signal %d \n\n\n",WSTOPSIG(status));

		if(WIFCONTINUED(status))
			printf("Process continued \n\n");
	}

return 0;
}
