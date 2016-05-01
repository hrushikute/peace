#include<stdio.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>
#include<dirent.h>
#include<stdlib.h>


void disp_dir(char *path,int ident)
{

	int ret_val;
	struct stat stat_buf;
	struct dirent *dp;
	DIR *d;
	//opne a directory
	d=opendir(path);
	if(d==NULL)
	{
		fprintf(stderr,"Cannot open the directory\n");
		return;
	}	
	chdir(path);
	printf("\nChanged the path TO :%s\n",path);
	//Read the directory conntent one by one
	while((dp=readdir(d)) != NULL)
	{
		printf("After performing readdir:%s\n",dp->d_name);
		//the stats for the file
		//ret_val=stat(dp->d_name,&stat_buf);a
		stat(dp->d_name,&stat_buf);
		if(ret_val==-1)
		{
			printf("Unble get the stat:\n");
			perror("Unable to get the stat :\n");
			return ;
		}
		printf("Sucessfully got the stats :%d",ret_val);
			
		if(S_ISDIR(stat_buf.st_mode))
		{
			//Found the directory

			printf("%*s%s-->%9d\n",ident,"",dp->d_name,stat_buf.st_size);
			
			disp_dir(dp->d_name,ident+4);
		}	
	
		else
			 printf("%*s%s-->%9d\n",ident,dp->d_name,stat_buf.st_size);

	}
	chdir("..");
	closedir(d);
}


int  main(int argc,char *argv[])
{

	printf("Directory to be scanned : /home/hrushi/peace\n");

	disp_dir("/home/hrushi/peace",0);

	return 0;

}
