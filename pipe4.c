#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<string.h>

int main (int argc, char *argv[])
{
 int result;
int filedesc;
char buffer [BUFSIZ+1];

memset(buffer,'\0',sizeof(buffer));


sscanf(argv[1],"%d",&filedesc);
result=read(filedesc,buffer,BUFSIZ);

printf("Process %d: Data raeda from the pipe: %s",getpid(), buffer);
exit(EXIT_SUCCESS);

return 0;
}

