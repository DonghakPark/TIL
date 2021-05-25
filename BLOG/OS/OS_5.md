## CPU Scheduling

---

### CPU and I/O Bursts in Program Execution

시스템은 I/O Burst, CPU Burst가 빈번하게 일어난다.

- 이는 프로그램의 종류에 따라서 상이하다.

- 특히 사람이 관여하는 프로그램일수록 번갈아 가면서 계속해서 일어난다.

이러한 여러 종류의 작업이 섞여 있기 때문에 CPU 스케듈링이 필요하다.

- Interactive job에게 적절한 response 제공 요망

- CPU와 I/O 장치 등 시스템 자원을 골고루 효율적으로 사용하기 위해서

프로세스의 특성 분류

- 프로세스는 그 특성에 따라 다음 두 가지로 나눔

  - I/O-bound Process

    - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job (many short cpu bursts)

  - CPU-bound Process

    - 계산 위주의 job (few very long CPU bursts)

---

### CPU Scheduler & Dispatcher

CPU Scheduler

- Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다.

Dispatcher

- CPU의 제어권을 CPU Scheduler에 의해 선택된 프로세스에게 넘긴다.
- 이 과정을 Context Switch라고 한다.

CPU 스케쥴링이 필요한 경우는 프로세스에게 다음과 같은 상태 변화가 있는 경우이다.

- Running -> Blocked (nonpremptive)

- Running -> Ready (preemptive)

- Blocked -> Ready (preemptive)

- Terminate (nonpreemptive)

  ***

### Scheduling Criteria (Performance Index)

CPU utilization (이용률)

- keep the CPU as busy as possible

Throughput (처리량)

- number of processes that complete their execution per time unit

Turnaround Time (소요시간, 반환시간)

- amount of time to execute a particular process

Waiting time (대기 시간)

- amount of time a process has been waiting in the ready queue

Response time (응답 시간)

- amount of time it takes from when a request was submitted until the first response is produced not output (for time sharing environment)

---

### Schedulting Algorithms

---

#### FCFS (First Come First Served)

- 프로세스가 도착한 순서대로 처리하는 알고리즘 (비선점형 알고리즘)

- Convoy Effect : 짧은 작업들이 긴 작업들 뒤에 있어서, 오래 기다리게 되는 현상 (CS에서)

---

#### SJF (Shortest Job First)

- 각 프로세스의 다음 CPU Burst가 가장 짧은 프로세스를 제일 먼저 스케쥴

- 비선점형 : 일단 CPU를 잡으면 이번 Burst가 끝날때까지 CPU를 선점 당하지 않음

- 선점형 : 현재 수행중인 프로세스의 남은 burst time보다 더 짧은 CPU burst time을 가지는 새로운 프로세스가 도착하면 CPU를 빼앗김

  - 이를 보고 (SRTF--> Shortest Remaining Time First)라고 부른다.

- 주어진 프로세스들에 대해 Minimum Average Waiting Time을 보장해준다.

- 문제점 : STF는 기아상태가 발생할 수 있다.

- 문제점 : CPU 사용 시간을 예측하기 힘들다.(과거의 정보를 통해서 추정하기 때문에, exponential averaging을 활용해서)

---

#### Priority Scheduling

A priority number is associated with each process

높은 우선순위를 가진 CPU에게 CPU를 우선 할당 (선점 or 비선점 식으로)

SJF는 일종의 우선순위 스케쥴링 기법이다.

문제점 : 기아현상(Starvation) -> low priority processes may never execute

해결법 : 에이징(Aging) -> as time processes increase the priority of the process

---

#### Round Robin (RR)

각 프로세스는 동일한 크기의 할당 시간을 가짐 (응답 시간이 빠름)

할당 시간이 지나면 프로세스는 선점당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다.

n개의 프로세스가 ready queue에 있고 할당 시간이 q time unit인 경우 각 프로세스는 최대 q time unit 단위로 CPU시간의 1/n을 얻는다. --> 어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다.

- q가 너무 크면 FCFS와 같다.

- q가 너무 작으면 context switch의 오버헤드가 커진다.

---

#### Multilevel Queue

Ready Queue를 여러 개로 분할해서 작업을 분산시키는 방법

- foreground (interactive)

- background (batch-no human interaction)

각 큐는 독립적인 스케쥴링 알고리즘을 가짐

- foreground : RR

- background : FCFS

큐에 대한 스케쥴링이 필요

- Fixed priority scheduling

  - serve all from foreground then from background

  - possibility of starvation

- Time Slice

  - 각 큐에 CPU time을 적절한 비율로 할당

### MLFQ : Multi Level Feedback Queue

프로세스가 다른 큐로 이동 가능한 MLQ

에이징을 이와 같은 방식으로 구현할 수 있다.

Multilevel feedback queue scheduler를 정의하는 파라미터

- Queue의 수

- 각 큐의 scheduling algorithm

- Process를 상위 큐로 보내는 기준

- Process를 하위 큐로 내쫓는 기준

- 프로세스가 CPU 서비스를 받으려 할 때 들어갈 큐를 경정하는 기준

---

### Multi Processor Scheduling

CPU가 여러 개인 경우 스케쥴링은 더욱 복잡해짐

Homogeneous Porcessor인 경우

- Queue에 한줄로 세워서 각 프로세스가 알아서 꺼내가게 할 수 있다.

- 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 더 복잡해짐

Load Sharing

- 일부 프로세서에 작업이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요

- 별개의 큐를 두는 방법 or 공동 큐를 사용하는 방법

Symmetric Multiprocessing (SMP)

- 각 프로세서가 각자 알아서 스케쥴링 결정

Asymmetric Multiprocessing

- 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

---

### Real Time Scheduling

Hard real time systems

- Hard Real time Task는 정해진 시간 안에 반드시 끝내도록 스케줄링

Soft real time systems

- Soft Real Time Task는 일반 프로세스에 비해 높은 priority를 갖도록 함

---

### Thread Scheduling

Local Scheduling

- User Level Thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정

Global Scheduling

- kernel level thread의 경우 일반 프로세스와 마찬 가지로 커널의 단기 스커줄러가 어떤 thread를 스케줄할지 결정

---

### Algorithm Evaluation

Queueing models

- 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 performance index 값을 계산

Implementation & Measurement

- 실제 시스템에 알고리즘을 구현하여 실제 작업(workload)에 대해서 성능을 측정 비교

Simulation

- 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과 비교

### Process Synchronization 문제

공유 데이터의 동시 접근은 데이터의 불일치 문제를 발생시킬 수 있다.

일관성을 유지하기 위해서는 협력 프로세스간의 실행 순서를 정해주는 매커니즘이 필요

Race Condition

- 여러 프로세스들이 동시에 공유 데이터를 접근하는 상황

- 데이터의 최종 연산 결과는 마지막에 그 데이터를 다룬 프로세스에 따라 달라짐

Race Condition을 막기 위해서는 Concurrent Process는 동기화 되어야 한다.

### Critical Section Problem

N개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우

각 프로세스의 code segment에는 공유 데이터를 접근하는 코드인 critical section이 존재

Problem : 하나의 프로세스가 critical section에 있을 때 다른 모든 프로세스는 critical section에 들어갈 수 없어야 한다.
