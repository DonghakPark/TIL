/*
*	DKU Operating System Lab
*	    Lab1 (Scheduler Algorithm Simulator)
*	    Student id : 32151648 / 32155068
*	    Student name : 박동학 / 홍승기
*
*   lab1_sched.c :
*       - Lab1 source file.
*       - Must contains scueduler algorithm function'definition.
*
*/
#include "lab1_sched_types.h"

void Init_process1() // 첫번째 프로세스 케이스

{

	Task[0].Name = 'A';

	Task[0].Arrival = 0;

	Task[0].Service = 3;

	Task[0].RunTime[0] = 0;

	Task[0].RunTime[1] = 0;

	Task[0].RunTime[2] = 0;

	Task[0].Ticket = 60;

 

	Task[1].Name = 'B';

	Task[1].Arrival = 3;

	Task[1].Service = 6;

	Task[1].RunTime[0] = 0;

	Task[1].RunTime[1] = 0;

	Task[1].RunTime[2] = 0;

	Task[1].Ticket = 20;

 

	Task[2].Name = 'C';

	Task[2].Arrival = 4;

	Task[2].Service = 4;

	Task[2].RunTime[0] = 0;

	Task[2].RunTime[1] = 0;

	Task[2].RunTime[2] = 0;

	Task[2].Ticket = 10;

 

	Task[3].Name = 'D';

	Task[3].Arrival = 6;

	Task[3].Service = 5;

	Task[3].RunTime[0] = 0;

	Task[3].RunTime[1] = 0;

	Task[3].RunTime[2] = 0;

	Task[3].Ticket = 5;

 

	Task[4].Name = 'E';

	Task[4].Arrival = 8;

	Task[4].Service = 2;

	Task[4].RunTime[0] = 0;

	Task[4].RunTime[1] = 0;

	Task[4].RunTime[2] = 0;

	Task[4].Ticket = 5;

 

	char Print[200] = { '\0' };

}

void Init_process2() //두번째 프로세스 

{

	Task[0].Name = 'A';

	Task[0].Arrival = 0;

	Task[0].Service = 2;

	Task[0].RunTime[0] = 0;

	Task[0].RunTime[1] = 0;

	Task[0].RunTime[2] = 0;

	Task[0].Ticket = 40;

 

	Task[1].Name = 'B';

	Task[1].Arrival = 3;

	Task[1].Service = 7;

	Task[1].RunTime[0] = 0;

	Task[1].RunTime[1] = 0;

	Task[1].RunTime[2] = 0;

	Task[1].Ticket = 20;

 

	Task[2].Name = 'C';

	Task[2].Arrival = 7;

	Task[2].Service = 10;

	Task[2].RunTime[0] = 0;

	Task[2].RunTime[1] = 0;

	Task[2].RunTime[2] = 0;

	Task[2].Ticket = 10;

 

	Task[3].Name = 'D';

	Task[3].Arrival = 13;

	Task[3].Service = 5;

	Task[3].RunTime[0] = 0;

	Task[3].RunTime[1] = 0;

	Task[3].RunTime[2] = 0;

	Task[3].Ticket = 15;

 

	Task[4].Name = 'E';

	Task[4].Arrival = 17;

	Task[4].Service = 2;

	Task[4].RunTime[0] = 0;

	Task[4].RunTime[1] = 0;

	Task[4].RunTime[2] = 0;

	Task[4].Ticket = 15;

 

}

int power(int x, int y)
{
	int result =1;
	while(y)
	{
		if(y&1)
		{	result *=x;
		}	
		y >>= 1;
		x *=x;
	}

	return result;

} //지수승을 구형 하기 위한 함수 

void InitQueue(Queue *queue)

{

	queue->front = queue->rear = NULL; //front와 rear를 NULL로 설정

	queue->count = 0;//보관 개수를 0으로 설정

} //queue를 
 

int IsEmpty(Queue *queue)

{

	return queue->count == 0;    //보관 개수가 0이면 빈 상태

}

 

void Enqueue(Queue *queue, process *data)

{

	Node *now = (Node *)malloc(sizeof(Node)); //노드 생성

	now->data = data;//데이터 설정

	now->next = NULL;

 

	if (IsEmpty(queue))//큐가 비어있을 때

	{

		queue->front = now;//맨 앞을 now로 설정       

	}

	else//비어있지 않을 때

	{

		queue->rear->next = now;//맨 뒤의 다음을 now로 설정

	}

	queue->rear = now;//맨 뒤를 now로 설정   

	queue->count++;//보관 개수를 1 증가

}

 

Node *Dequeue(Queue *queue)

{

	Node *re = 0;

	Node *now;

	if (IsEmpty(queue))//큐가 비었을 때

	{

		return re;

	}

	now = queue->front;//맨 앞의 노드를 now에 기억

	re = now;//반환할 값은 now의 data로 설정

	queue->front = now->next;//맨 앞은 now의 다음 노드로 설정

	free(now);//now 소멸

	queue->count--;//보관 개수를 1 감소

	return re;

}

////////////////////////////////////////////////////////////////////////////////////

void Draw()

{

	int i = 0;

 

	printf("Task 1 | ");

	while (Print[i] != '\0')

	{

		if (Print[i] == 'A')

		{

			printf("■ ");

			i++;

		}

		else

		{

			if (Print[i] != 'A')

			{

				printf("□ ");

				i++;

			}

			continue;

		}

	}

 

 

	printf("\nTask 2 | ");

	i = 0;

	while (Print[i] != '\0')

	{

		if (Print[i] == 'B')

		{

			printf("■ ");

			i++;

		}

		else

		{

			if (Print[i] != 'B')

			{

				printf("□ ");

				i++;

			}

			continue;

		}

	}

 

	printf("\nTask 3 | ");

	i = 0;

	while (Print[i] != '\0')

	{

		if (Print[i] == 'C')

		{

			printf("■ ");

			i++;

		}

		else

		{

			if (Print[i] != 'C')

			{

				printf("□ ");

				i++;

			}

			continue;

		}

	}

	printf("\nTask 4 | ");

	i = 0;

	while (Print[i] != '\0')

	{

		if (Print[i] == 'D')

		{

			printf("■ ");

			i++;

		}

		else

		{

			if (Print[i] != 'D')

			{

				printf("□ ");

				i++;

			}

			continue;

		}

	}

	printf("\nTask 5 | ");

	i = 0;

	while (Print[i] != '\0')

	{

		if (Print[i] == 'E')

		{

			printf("■ ");

			i++;

		}

		else

		{

			if (Print[i] != 'E')

			{

				printf("□ ");

				i++;

			}

			continue;

		}

	}

	printf("\n");

} // 구현한 스케쥴링에 대한 그림을 그려주는 함수 

void FCFS(process a, process b, process c, process d, process e)

{

	Queue FiFO_Queue; int Blank_count = 0;

	InitQueue(&FiFO_Queue);

	int time = a.Service + b.Service + c.Service + d.Service + e.Service; //전체 수행시간을 

	int G = time; //기준 시간을 

	int time_count = 0; // 시간이 얼마나 흘렀는지 

	for (int i = 0; i < 5; i++)

	{

		if (0 == Task[i].Arrival)

		{

			Enqueue(&FiFO_Queue, &Task[i]);

		}

	}//도착시간이 0인 것을 Enqueue

 

	while (time != 0)

	{

		if (!IsEmpty(&FiFO_Queue))

		{

			Print[time_count] = FiFO_Queue.front->data->Name;

			FiFO_Queue.front->data->Service--;

			time_count++;

			time--;

		}//서비스시간이 남았을 경우 

		else if (IsEmpty(&FiFO_Queue))

		{

			Print[time_count] = 'X';

			time_count++;

		} // 큐가 비었을 경우를 체크 ( 공백이 생기는 경우를 )

		for (int i = 0; i < 5; i++)

		{

			if (time_count == Task[i].Arrival)

			{

				Enqueue(&FiFO_Queue, &Task[i]);

			}

		}

		//도착시간을 체크하여 도착 순서대로 큐에 

		if ((FiFO_Queue.front->data->Service == 0))

		{

			Dequeue(&FiFO_Queue);

		} // 서비스 타임이 끝난 프로세스를 큐에서 


	}

	printf("--------------- FCFS ---------------\n");

	Draw(); //그림그리기

}


void RR(process a, process b, process c, process d, process e, int t)

{

	int time_Slice = t; //타임 퀀텀

	int time_count = 0;

	int time = a.Service + b.Service + c.Service + d.Service + e.Service;

	Queue RR_Queue;

	InitQueue(&RR_Queue);

 

	for (int i = 0; i < 5; i++)

	{

		if (0 == Task[i].Arrival)

		{

			Enqueue(&RR_Queue, &Task[i]);

		}

	}//도착시간이 0인 것을 Enqueue

 

	while (time != 0)

	{

		if (!IsEmpty(&RR_Queue))

		{

			Print[time_count] = RR_Queue.front->data->Name;

			RR_Queue.front->data->Service--;

			RR_Queue.front->data->RunTime[0]++;

			time_count++;

			time--;

		} // 큐에 프로세스가 있는 경우 

		else if (IsEmpty(&RR_Queue))

		{

			Print[time_count] = 'X';

			time_count++;

		} // 큐가 비었을 경우

 

		for (int i = 0; i < 5; i++)

		{

			if (time_count == Task[i].Arrival)

			{

				Enqueue(&RR_Queue, &Task[i]);

			}

		} // 실행중에 들어오는 프로세스가 있는지 검사 

		if (RR_Queue.front->data->RunTime[0] == 0)//공백이 생기는 특수한 경우를 

		{

			Print[time_count] = RR_Queue.front->data->Name;

			RR_Queue.front->data->Service--;

			RR_Queue.front->data->RunTime[0]++;

			time_count++;

			for (int i = 0; i < 5; i++)

			{

				if (time_count == Task[i].Arrival)

				{

					Enqueue(&RR_Queue, &Task[i]);

				}

			}

			time--;

		}

		if (RR_Queue.front->data->Service != 0 && (RR_Queue.front->data->RunTime[0]) % (time_Slice) == 0)

		{

			Enqueue(&RR_Queue, RR_Queue.front->data);

			Dequeue(&RR_Queue);

		}// 서비스 시간이 남았지만 타임퀀텀을 초과한 경우 다시 뒤로 보낸다.

		else if ((RR_Queue.front->data->Service == 0))

		{

			Dequeue(&RR_Queue);

		} //서비스 타임을 초과한 경우 큐에서 뺀다

 

	}

 

	printf("--------------- R R ---------------\n");

	Draw();

}


void Lottery(process a, process b, process c, process d, process e)

{

	srand((unsigned)time(NULL)); //매 실행마다 랜덤수가 달라지게 설정

 

	int time = Task[0].Service + Task[1].Service + Task[2].Service + Task[3].Service + Task[4].Service;

	int ticket[100]; //티켓을 저장할 

	int count = 0; // 프로세스 번호

	int i = 0;

	int Ticket_count = 0;

	int print_count = 0;

 

 

 

	for (int i = 0; i<100; i++)

	{

		ticket[i] = (rand() % 100);

		for (int j = 0; j<i; j++)

		{

			if (ticket[j] == ticket[i])

			{

				i--;

				break;

			}

		} 

	} //랜덤한 수 입력

 

	while (time != 0)//총 수행시간 까지 반복

	{

		if (count == 0) //첫 입력이거나 해당 프로세스를 찾아 초기화 된 

		{

			Ticket_count = 0 + Task[count].Ticket;

		}

		if (Task[count].Service != 0 && Ticket_count > ticket[i]) //해당하는 티켓을 찾았을 

		{

			Print[print_count] = Task[count].Name;

			Task[count].Service--;

			Ticket_count = 0;

			count = 0;

			time--; i++;

			print_count++;

		}

		else if (Task[count].Service == 0) //서비스 타임이 

		{

			count++;

			if (ticket[i] < Ticket_count)

			{

				if (count > 4)

				{

					count = 0;

					Ticket_count = 0;

				}

				for (int j = 0; j < 100; j++)

				{

					i++;

					if (ticket[i] > Ticket_count)

					{

						break;

					}

				}

				Ticket_count = Ticket_count + Task[count].Ticket;

				if (i >= 100)

				{

					i = 0;

				}

			}

			else

			{

				Ticket_count = Ticket_count + Task[count].Ticket;

				if (count > 4)

				{

					count = 0;

					Ticket_count = 0;

				}

			}

		}

		else

		{

			count++;

			Ticket_count = Ticket_count + Task[count].Ticket;

			if (count > 4)

			{

				count = 0;

				Ticket_count = 0;

 

			}

		}

 

	}

	printf("--------------- Lottery ---------------\n");

	Draw();

 

}

//////////////////////////////////////////////////////////////////////////////////////

void MLFQ(process a, process b, process c, process d, process e, int t)

{

	int time_Slice = t;

	int time_count = 0;

	int time = a.Service + b.Service + c.Service + d.Service + e.Service;

	int G = time;

	Queue Priorirty_1;

	Queue Priorirty_2;

	Queue Priorirty_3;

	InitQueue(&Priorirty_1);

	InitQueue(&Priorirty_2);

	InitQueue(&Priorirty_3);

 

	for (int i = 0; i < 5; i++)

	{

		if (0 == Task[i].Arrival)

		{

			Enqueue(&Priorirty_1, &Task[i]);

		}

	}//도착시간이 0인 것을 1번 큐에 삽입

 

	while (time != 0)

	{

		////////////////////////////////////////////1번째 우선순위를 가지는 

		if (!IsEmpty(&Priorirty_1))

		{

			for (int i = 0; i < power(time_Slice, 0); i++) //타임 슬라이스 만큼 수행 

			{

				Print[time_count] = Priorirty_1.front->data->Name;

				Priorirty_1.front->data->Service--;

				Priorirty_1.front->data->RunTime[0]++;

			}

			time_count++;

			time--;

		}

		else if (IsEmpty(&Priorirty_1)) // 큐가 비었을 

		{

			Print[time_count] = 'X';

			time_count++;

		}

		for (int i = 0; i < 5; i++)

		{

			if (time_count == Task[i].Arrival)

			{

				Enqueue(&Priorirty_1, &Task[i]);

			}

		} // 새로 도착하는 큐가 있는지 

		if (Priorirty_1.front->data->RunTime[0] == 0) //공백의 경우 

		{

			for (int i = 0; i < power(time_Slice, 0); i++)

			{

				Print[time_count] = Priorirty_1.front->data->Name;

				Priorirty_1.front->data->Service--;

				Priorirty_1.front->data->RunTime[0]++;

			}

			time_count++;

			for (int i = 0; i < 5; i++)

			{

				if (time_count == Task[i].Arrival)

				{

					Enqueue(&Priorirty_1, &Task[i]);

				}

			}

			time--;

		}

		if (!IsEmpty(&Priorirty_1) && Priorirty_1.front->data->Service != 0 && (Priorirty_1.front->data->RunTime[0]) % (int)power(time_Slice, 0) == 0)

		{ // 수행시간은 끝나지 않았지만 타임슬라이스가 끝난 

			if (Priorirty_1.front->next == NULL && IsEmpty(&Priorirty_2) && IsEmpty(&Priorirty_3))

			{

				Enqueue(&Priorirty_1, Priorirty_1.front->data);

				Dequeue(&Priorirty_1);

			} // 큐에 혼자 

			else

			{

				Enqueue(&Priorirty_2, Priorirty_1.front->data);

				Dequeue(&Priorirty_1);

			} // 아닐 경우 우선순위 

		}

		else if ((Priorirty_1.front->data->Service == 0))

		{

			Dequeue(&Priorirty_1);

		}

		////////////////////////////////////////////////////2번째 

		while (IsEmpty(&Priorirty_1))

		{

			if (!IsEmpty(&Priorirty_2))

			{

				for (int i = 0; i < power(time_Slice, 1); i++)

				{

 

					Print[time_count] = Priorirty_2.front->data->Name;

					Priorirty_2.front->data->Service--;

					Priorirty_2.front->data->RunTime[1]++;

 

					time_count++;

					time--;

					for (int i = 0; i < 5; i++)

					{

						if (time_count == Task[i].Arrival)

						{

							Enqueue(&Priorirty_1, &Task[i]);

						}

					}

					if (IsEmpty(&Priorirty_1))

						break;

					if (Priorirty_2.front->data->Service == 0)

					{

						break;

					}

				}

			}

			if (!IsEmpty(&Priorirty_2) && Priorirty_2.front->data->Service != 0 && ((Priorirty_2.front->data->RunTime[1]) % (int)power(time_Slice, 1)) == 0)

			{

				Enqueue(&Priorirty_3, Priorirty_2.front->data);

				Dequeue(&Priorirty_2);

			}

			else if (!IsEmpty(&Priorirty_2) && (Priorirty_2.front->data->Service == 0))

			{

				Dequeue(&Priorirty_2);

			}

			else if (IsEmpty(&Priorirty_2))

				break;

		}

		/////////////////////////////////////////////////// 3번째 

		while (IsEmpty(&Priorirty_1) && IsEmpty(&Priorirty_2))

		{

			if (!IsEmpty(&Priorirty_3))

			{

				for (int i = 0; i < power(time_Slice, 2); i++)

				{

					Print[time_count] = Priorirty_3.front->data->Name;

					Priorirty_3.front->data->Service--;

					Priorirty_3.front->data->RunTime[2]++;

					time_count++;

					time--;

					for (int i = 0; i < 5; i++)

					{

						if (time_count == Task[i].Arrival)

						{

							Enqueue(&Priorirty_1, &Task[i]);

						}

					}

					if (IsEmpty(&Priorirty_1))

						break;

					if (Priorirty_3.front->data->Service == 0)

					{

						break;

					}

				}

			}

 

			if (!IsEmpty(&Priorirty_3) && Priorirty_3.front->data->Service != 0 && (Priorirty_3.front->data->RunTime[2]) % (int)(power(time_Slice, 2)) == 0)

			{

				Enqueue(&Priorirty_3, Priorirty_3.front->data);

				Dequeue(&Priorirty_3);

			}

			else if (!IsEmpty(&Priorirty_3) && (Priorirty_3.front->data->Service == 0))

			{

				Dequeue(&Priorirty_3);

			}

 

			if (IsEmpty(&Priorirty_3))

				break;

 

		}

 

	}

 

	printf("--------------- M L F Q ---------------\n");

	Draw();

}

