// Created by Meagan Kropp

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	char str[256];
	int counter = 0;
	printf("$ ");
	fgets(str, 256, stdin);	//gets user info		


	//loops till meets exit requirements, i.e. user inputs exit
	while(strcmp(str, "exit\n") != 0) 
	{
		printf("Line read: ");
		fputs(str,stdout);
		printf("Token(s): ");
	
		//goes to next token, decided by space between the items
		char* token = strtok(str, " ");
		while (token != NULL)
		{
			counter++;
			printf(" \n%s", token);
			token = strtok(NULL, " ");
		}
		printf("%d token(s) read\n", counter);
		printf("\n");
		printf("$ ");
		fgets(str, 256, stdin);
		counter = 0;
	}
	return 0;
}
