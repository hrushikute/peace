#include <stdio.h>
#include<sys/types.h>
#include<dirent.h>
#include<stdlib.h>
int main (int argc,char *argv[])
{

	DIR *dir;
	struct dirent *sd;
	dir=opendir(".");
	
	if(dir == NULL)
	{
		printf("ERROR: Unable to open directory. \n");
		exit(1);
	}
	
	while((sd=readdir(dir))!=NULL)
	{
		printf(">>%c  %s\n",sd->d_type,sd->d_name);
		
	}

	return 0;
}
