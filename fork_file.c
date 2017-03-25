 #include<stdio.h>
#include<unistd.h>

int main (int argc , char *argv[])
{

	int counterp,childpid;

	printf("BEfore running the Fork the parent process ID :  %d \n",getpid());

	childpid=fork();

	if(childpid == 0)
	{
	

		printf("\n\nTHis is a child process :%d\n",getpid());





	}

	else
	{
	
		printf("This is Parent process : %d",getpid());

	}


	return 0;

}	
