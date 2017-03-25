#include <stdio.h>

int main (int agec, char *argv[])
{


	int a[10] = { 4, 2, 10, 34, 23, 54, 21, 29, 32, 43 };
	int s_counter=0,r_counter;
	int hold;
	int length=sizeof(a)/sizeof(int);
	printf ("lenght=%d \n",length);

	for (s_counter=0;s_counter<length;s_counter++)
	{
		printf("a[%d]=%d \n",s_counter,a[s_counter]);

	}

	for(r_counter=length-1;r_counter>0;r_counter--)
	{

		for (s_counter=0;s_counter<r_counter;s_counter++)
		{
			if(a[s_counter]>a[s_counter+1])
			{ 
				

				hold=a[s_counter];
				a[s_counter]=a[s_counter+1];
				a[s_counter+1]=hold;
	
			}
		}	


	}



	for (s_counter=0;s_counter<length;s_counter++)
	{
		printf("a[%d]=%d \n",s_counter,a[s_counter]);

	}	



	return 0;
}
