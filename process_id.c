#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main (int argc,char * argv[])
{
	pid_t process_id_child,process_id_parent;

	process_id_child = getpid();
	process_id_parent=getppid();


	printf(" Parent Process ID: %d \n",process_id_parent);


	printf(" Child Process ID: %d \n",process_id_child);

return 0;
}
