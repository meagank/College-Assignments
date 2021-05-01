//Created by Meagan Kropp


#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <string.h>
#include <sys/wait.h>


int main(int argc, char *argv[])
{
	if(argc == 1)
	{
		printf("Usage: %s <dir>\n", argv[0]);
		exit(1);
	}

	pid_t p = fork();
	if(p == 0) // child process
	{
		char temp[256];
		printf("Current working directory: %s\n",temp);
		printf("Executing ls %s -l -h\n", argv[1]);

		int ch = chdir(argv[1]);
		if (ch == 0)
		{
			execl("/bin/ls", "ls", "-l", NULL);
			exit(0);
		}
		else
		{
			printf("Can't chdir to %s\n", argv[1]);
			exit(1);
		}
	}
	else
	{
		int status;
		wait(&status);
		printf("Exit status: %d\n", status>>8);
	}		
	return 0;
	
}
