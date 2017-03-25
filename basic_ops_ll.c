#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

struct node
{
int data;
struct node *next;
};

struct node *head;

void insert(int);
void display();
void delete();

int main(int argc,char* argv[])
{

int option=0,data;


while(option !=9)
{

printf ("\n****************************\n Welcome to linked list operation.\n CHoose from below choices.\n");
printf("1.Insert node.\n");
printf("2.Delete node.\n");
printf("3.Display linked list.\n");
printf("9.Exit from programi.\n");
printf("*****************************\nEnter the option:");
scanf("%d",&option);


switch(option)
{
	case 1:
		printf("Enter the number: ");	
		scanf("%d",&data);
		insert( data);
		break;


	case 2:
		delete();
		break;



	case 3: printf("Below is the data in list:\n");
		display();
		break;
	
	case 9:
		{
			printf("Good Bye !!!");
			exit(EXIT_SUCCESS);
		}
	

}

}

return 0;

}


// Function ot insert the dat in linked list.

void insert(int data)
{

struct node *new_node,*traverse;
new_node=(struct node *)malloc(sizeof(struct node));

new_node->data=data;
new_node->next=NULL;
if(head==NULL)
{

	head=new_node;
}
else
{
	traverse=head;

	while(traverse->next!=NULL)
		traverse =traverse->next;

	traverse->next=new_node;

}

}





// Function to display the data in linked list.


void display()
{

struct node *traverse;
if (head==NULL)
{
	printf("List is empty !\n");
}
else
{
	traverse=head;
	 do
	{

		printf("%d-->",traverse->data);
		traverse=traverse->next;
	}while(traverse!=NULL);


	
}

}

void delete()
{

struct node *traverse,*previous;

if(head==NULL)
{
	printf("List is laready empty cant delete now !\n\n ");

}
else if(head->next==NULL)
{
	traverse=head;
	free(traverse);
}
	
else
{
	
	traverse=head;
	previous=traverse;
	while(traverse->next!=NULL)
	{
		previous=traverse;
		traverse=traverse->next;
	}
	previous->next=NULL;
	free(traverse);	
}
}
