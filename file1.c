#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>

int main (int argc, char *argv[])
{
	struct stat stat_buf;
//	char file_name[1024];
//	file_name=argv[1];
	
	//get the stats of file 

	stat("message.h",&stat_buf);
	printf("message,h-->%9d",stat_buf.st_size);
	return 0;

}
