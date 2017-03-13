#include <stdio.h>

#ifndef WIN32
#include <unistd.h>
#endif

#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
#include <time.h>

#include "outback.h"

#define MB_SERV_PORT		502
#define DEF_SERV_IP_ADDR	"192.168.2.220"

int main(void)
{
	
	int	devices	= 0;
	int	connected = 0;
	char buff[128];
	char address[16];
	int	i, j;
	char command = 0;
	int	block;
	int	field;
	int mb_port = MB_SERV_PORT;
	
	printf("OutBack Commnunications Shell\n\n");
	printf("Version 3.0.105\n");
}