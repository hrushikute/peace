/*Program to write the data to standard output*/

#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>

int main (int argc, char* argv[])
{

	int num_read,i;
	num_read=open("myfile1",O_CREAT,0777);
	printf("\nFile_descripto:%d\n",num_read);
i=write(num_read,"Hi Whats up guys?\n",40);
	printf("Num read:%d\n",i);
	close(num_read);
	return 0;
}
