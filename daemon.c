#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include </usr/include/linux/fs.h>
#undef NR_OPEN
#define NR_OPEN 256

int main(int argc , char *argv[])
{

	pid_t proc_id;
	int i,ret;

	/*Step 1 : Create a new process*/
	
	proc_id=fork();

	if (proc_id == -1 )
		return -1;

	else if (proc_id !=0)
		exit(EXIT_SUCCESS);

	/*Step 2: Crete new session and process group*/

	if (setsid()==-1)
		return -1;
	
	/*Step 3: Set working directory to root */
	if (chdir("/") == -1)
		return -1;

	/*step 4: close all the open files --NR_OPEN */
	for (i = 0;i < NR_OPEN; i++)
		close(i);

	/*Step 5: Redirect all the fd 0 1 2 to /dev/null.*/

	open("/dev/null",O_RDWR); /*stin*/
	dup(0);			 /*stout*/	
	dup(0);			 /*stderror*/


	/*Step 6:My daemon thing !!!*/

	ret=system("ls -lrt");
//	if(WIFSIGNALED(ret)&&(WTERMSIF (ret)==SIGINT || WTERMSIG(ret)==SIGQUIT))
//	{
//		printf("system error !");
//		perror("system");
//	}
	sleep (5);



return 0;
}
