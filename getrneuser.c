#include<unistd.h>
#include<sys/types.h>
#include <stdio.h>
int main (int argc, char *argv[])
{

uid_t r,e;

uid_t getuid(void);
uid_t getgid(void);

printf("Real User Id: %d\n\n",getuid());

printf("Effective User Id: %d\n\n",getgid());


printf("Process  Id: %d\n\n",getpid());


printf("Process Gruop Id: %d\n\n",getpgrp());

return 0;
}
