## Process

: Process is a program in execution (프로세스는 실행중인 프로그램이다.)

---

### 프로세스의 문맥 (Context)

현재 프로세스의 특정 시점에 어떤 작업을 했는지, 어떤 상태인지를 알 수 있는 정보

CPU 수행 상태를 나타내는 하드웨어 문맥

- Program Counter
- 각종 Register

프로세스의 주소 공간

- Code, Data, Stack

프로세스 관련 커널 자료 구조

- PCB (Process Control Block)
- Kernel Stack

---

### Process State (프로세스의 상태)

프로세스는 상태가 변경되며 수행된다.

- Running : CPU를 잡고 Instruction을 수행중인 상태

- Ready : CPU를 기다리는 상태 (메모리 등 자른 조건을 모두 만족하고)

- Block(Wait, Sleep)

  - CPU를 주어도 당장 Instruction을 수행할 수 없는 상태
  - Process 자신이 요청한 이벤트가 즉시 만족되지 않아 이를 기다리는 상태

- suspended(stopped)

  - 외부적인 이유로 프로세스의 수행이 정지된 상태
  - 프로세스는 통째로 디스크에 swap out 된다.

- New : 프로세스가 생성중인 상태

- Terminated : 수행이 끝난 상태

---

### PCB (Process Control Block)

운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보

- OS가 관리상 사용하는 정보

  - Process State, Process ID
  - Scheduling Information, Priority

- CPU 수행 관련 하드웨어 값

  - Program Counter, Registers

- 메모리 관련

  - Code, Data, Stack의 위치 정보

- 파일 관련

---

### 문맥 교롼 (Context Switch)

CPU가 한 프로세스에서 다른 프로세스로 넘겨주는 과정

- CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
- CPU를 새롭게 얻은 프로세스는 상태를 PCB에서 읽어옴

-> 프로세스가 바뀔 때 발생

-> 모든 인터럽트 or System Call 마다 문맥교환이 발생하는 것은 아님

---

#### 프로세스를 스케쥴링하기 위한 큐

- job queue

  - 현재 시스템 내에 있는 모든 프로세스의 집합

- ready queue

  - 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합

- Device queues
  - I/O devoce의 처리를 기다리는 프로세스의 집합

프로세스들은 각 큐들을 오가며 수행된다.

---

### 스케줄러 (Scheduler)

Long term Scheduler (장기 스케줄러)

- 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
- 프로세스에 memory을 주는 문제
- degree of Multiprogramming을 제어
- Time Sharing System에는 보통 장기 스케줄러가 없음

Short term Scheduler (단기 스케줄러, CPU scheduler)

- 어떤 프로세스를 다음번에 Running 시킬지 결정
- Process에 CPU를 주는 문제
- 충분히 빨라야 함

Medium term Scheduler

- 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
- 프로세스에게서 메모리를 뺏는 문제
- degree of Multiprogramming을 제어

---

### Thread (쓰레드)

A Thread is a basic unit of CPU utilization

Thread의 구성

- Program Counter
- Register Set
- Stack Space

Thread가 공유하는 부분

- Code
- Data
- OS resources

즉, 실행 흐름만을 따로 두고, 여러 실행흐름으로 나누는 것을 쓰레드라고 한다.

쓰레드 사용의 장점

- 다중 스레드로 구성된 테스트 구조에서는 하나의 서버 스레드가 blocked 상태인 동안에도 동일한 테스트 내의 다른 스레드가 실행되어 빠른 처리를 할 수 있다.
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율과 성능 향상을 얻을 수 있다.
- 스레드를 사용하면 병렬성을 높일 수 있다.

따라서 크게 4가지의 장점으로 정리할 수 있다.

- Responsiveness
- Resource Sharing
- Economy
- Utilization of MP Architectures

Thread 구현 방법

- kernel Threads : 커널에서 Thread를 처리하게 됨
- User Threads : 라이브러리를 통해서 지원, 유저 프로그램 스스로 쓰레드 관리
