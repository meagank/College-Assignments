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
	if(argc != 2)
	{
		printf("Usage: %s <executable\n", argv[0]);
		printf("e.g., %s ./one.sh\n", argv[0]);
		exit(1);
	}

	srand(time(NULL));
	int numArg = rand() % (10 + 1) ;
	
	char args[numArg][3];
	for (int i = 0; i < numArg; i++)
	{
		snprintf(args[i],3, "%d",rand() % 10);
	}

	pid_t p = fork();
	if(p == 0) // in the child
	{
		char *execArgs[2 + numArg];
		execArgs[0] = strdup(argv[1]);
		for(int i = 0; i < numArg; i++)
		{
			execArgs[i+1] = strdup(args[i]);
		}
		execArgs[1 + numArg] = NULL;
		
		printf("In child %d: ", getpid());
		fflush(stdout);

		execvp(execArgs[0], execArgs);
		
	}
	else
	{
		wait(NULL);
	}
	return 0;
}


