/*
*	DKU Operating System Lab
*	    Lab1 (Scheduler Algorithm Simulator)
*	    Student id : 32151648, 32155068
*	    Student name : 박동학 , 
*
*   lab1_sched_types.h :
*       - lab1 header file.
*       - must contains scueduler algorithm function's declations.
*
*/

#ifndef _LAB1_HEADER_H
#define _LAB1_HEADER_H

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
#include <stddef.h>
#include "lab1_sched_types.h"



typedef struct process {

	char Name;

	int Arrival;

	int Service; //실행해야하는 시간

	int RunTime[3]; //실제 실행시간

	int Ticket;

}process;

char Print[200];
process Task[5];

typedef struct Node //노드 정의

{

	process *data;

	struct Node *next;

}Node;

typedef struct Queue //Queue 구조체 정의

{

	Node *front; //맨 앞(꺼낼 위치)

	Node *rear; //맨 뒤(보관할 위치)

	int count;//보관 개수

}Queue;

void Init_process1();
void Init_process2();
void InitQueue(Queue *queue);
int IsEmpty(Queue *queue);
void Enqueue(Queue *queue, process *data);
Node *Dequeue(Queue *queue);
void Draw();
void FCFS(process a, process b, process c, process d, process e);
void RR(process a, process b, process c, process d, process e, int t);
void Lottery(process a, process b, process c, process d, process e);
void MLFQ(process a, process b, process c, process d, process e, int t);
int power(int x, int y);





#endif /* LAB1_HEADER_H*/



