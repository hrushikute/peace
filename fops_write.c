/*Program to write the data to standard output*/

#include<stdio.h>
#include<unistd.h>

int main (int argc, char* argv[])
{

	write(1,"Hi How are you ?",20);
	return 0;
}
