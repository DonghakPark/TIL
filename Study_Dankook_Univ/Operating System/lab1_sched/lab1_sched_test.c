/*
*	DKU Operating System Lab
*	    Lab1 (Scheduler Algorithm Simulator)
*	    Student id : 32151648, 32155068
*	    Student name : 박동학 
*
*   lab1_sched.c :
*       - Lab1 source file.
*       - Must contains scueduler algorithm test code.
*
*/

#include <aio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h>
#include <sys/time.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <assert.h>
#include <pthread.h>
#include <asm/unistd.h>
#include <math.h>
#include "lab1_sched_types.h"

/*
 * you need to implement scheduler simlator test code.
 *
 */

int main(int argc, char *argv[]) {

	Init_process1(); // 1번째 케이스에 대한 테스트
	FCFS(Task[0], Task[1], Task[2], Task[3], Task[4]);

	Init_process1();
	RR(Task[0], Task[1], Task[2], Task[3], Task[4], 1);

	Init_process1();
	Lottery(Task[0], Task[1], Task[2], Task[3], Task[4]);

	Init_process1();
	MLFQ(Task[0], Task[1], Task[2], Task[3], Task[4], 1);
	//////////////////////////////////////////////////////
	Init_process2(); // 2번째 케이스에 대한 테스트
	FCFS(Task[0], Task[1], Task[2], Task[3], Task[4]);

	Init_process2();
	RR(Task[0], Task[1], Task[2], Task[3], Task[4], 1);

	Init_process2();
	Lottery(Task[0], Task[1], Task[2], Task[3], Task[4]);

	Init_process2();
	MLFQ(Task[0], Task[1], Task[2], Task[3], Task[4], 2);

	return 0;

}


