> 본 게시물은 KOCW의 반효경 교수님의 강의를 기반으로 정리한 것입니다.

## Process Synchronization [Concurrency Control] - 병행 제어, 프로세스 동기화

---

### 데이터의 접근

- 저장소의 데이터
- 연산할 데이터 전송
- 연산 수행
- 연산 결과 반환

: 데이터를 읽고 쓰기 때문에 데이터의 동기화가 필요하다.

---

### Race Condition

여러 프로세스가 하나의 데이터를 공유하고, 연산을 하려고 할 때 경쟁 상태가 생길 수 있다.

즉 하나의 데이터에 대한 여러 연산 요청이 있을 때는 이를 조절해 줘야한다는 것이다.

ex) Multiprocessor System, 공유메모리를 사용하는 프로세스들, 커널 내부 데이터를 접근하는 루틴들 간의 충돌 등등

---

### 프로그램적 해결법의 충족 조건

Mutual Exclusion (상호 배제) : 배타적으로 접근해야 한다.

- 프로세스가 임계영역 부분을 수행중이면 다른 모든 프로세스들은 그들의 임계영역에 들어가면 안 된다.

Progress : 비어있을 때는 사용하게 해줘야 한다.

- 아무도 임계영역에 있지 않은 상태에서 임계영역에 들어가고자 하는 프로세스가 있으면 임게영역에 들어가게 해주어야한다.

Bounded Waiting : 기다리는 시간이 유한해야 한다.

- 프로세스가 임계영역에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 임계영역에 들어가는 횟수에 한계가 있어야한다.

가정

- 모든 프로세스의 수행 속도는 0보다 크다.

- 프로세스들 간의 상대적인 수행 속도는 가정하지 않는다.

#### Algorithm 1

Synchronization variable

- 변수를 통해서 임계영역에 들어갈 프로세스를 정해준다.

```c
do {
    while (turn != 0)
    critical section
    turn = 1;
    remainder section
} while (1);

}
```

--> Mutual Exclusiong은 만족, Progress는 만족 X : 위의 알고리즘은 상대방이 사용해야지만 자신이 한번 사용할 수 있는 알고리즘이다.

#### Algorithm 2

플래그를 사용

```c
do {
    flag[i] = true;
    while(flag[j]);
    critical section
    flag[i] = false;
    remainder section
} while(1);

```

--> Mutual Exclusion 만족, Progress 만족 X : 동시에 수행하려고 하면 계속해서 서로를 대기하는 문제가 발생할 수 있음

#### Algorithm 3

Turn, Flag를 모두 사용

```c
do {
    flag[i]= true;
    turm = j;
    while(flag[j] && turn == j);
    critical section
    flag[i] = false;
    remainder section
} while(1);
```

--> 모든 요구 조건을 만족, Busy Waiting(Spin Lock)!!!

---

### Synchronization Hardware

하드웨어적으로 Test & modify를 Atomic하게 수핼할 수 있도록 지원하는 경우 앞의 문제는 간단하게 해결가능

```c
Synchronization variable;
    boolean lock = false;

do {
    while(Test_and_Set(losk));
    critical section
    lock = false;
    remainder section
}
```

--> 이러한 작업들을 추상화 시킨것이 Semaphores

---

### Semaphores

Semaphore S (추상자료형)

- Integer Variable (자원의 갯수)

- 아래의 두가지 Atomic 연산에 의해서만 접근 가능

  - P(S): while (S<=) do no-op; S--; --> 공유자원을 획득하는 연상

  - V(S) : S++; --> 반납하는 연산

### Block / Wakeup Implementation

Semaphore를 다음과 같이 정의

```c
typedef struct
{
    int value;
    struct process *L;
}semaphore;
```

block 과 wakeup을 다음과 같이 지정

- block : 커널은 block을 호출한 프로세스를 suspend시킴, 이 프로세스의 PCB를 semaphore에 대한 wait queue에 넣음

- wakeup(P) : block된 프로세스 P를 wakeup시킴, 이 프로세스의 PCB를 ready queue로 옮김

Busy wait vs Block/wakeup

- Critical Section의 길이가 긴 경우 Block/Wakeup이 적당

- Critical Section의 길이가 매우 짧은 경우 Blcok/Wakeup 오버헤드가 Busy-wait 오버헤드보다 더 커질 수 있음

- 일반적으로는 Block/wakeup 방식이 더 좋음

이러한 Semaphores는 2가지로 나눌 수 있음

- Counting Semapgore : 자원의 갯수가 여러개인 경우

  - 도메인이 0이상인 임의의 정수값

  - 주로 Resouce Counting에 사용

- Binary Semaphore (mutex) : 자원이 1개인 경우

  - 0 또는 1 값만 가질 수 있는 Semaphore

  - 주로 Mutual Exclusion (lock / unlock)에 사용

### Deadlock and Starvation

Deadlock

- 둘 이상의 프로세스가 서로 상대방에 의해 충족될 수 있는 event를 무한히 기다리는 현상

Starvation

- Infinite blocking : 프로세스가 suspend된 이유에 해당되는 세마포어 큐에서 빠져나갈 수 없는 현상

---

### 동기화와 관련된 고전 문제

#### Bounded - Buffer Problem (Producer Consumer Problem)

Producer 여러개, Consumer가 여러개인 상황이다. 따라서 다음과 같은 문제가 생길 수 있다.

Shard data

- buffer 자체 및 buffer 조작 편수 (empty/full buffer의 시작 위치)

Synchronization variables

- mutual exclusion : Need Binary Semaphore

- resource count : Need integer Semaphore

발생 가능한 동기화 문제

- 공유 버퍼이기 때문에 생산자가 동시에 버퍼에 데이터를 쓰거나 수정하면 안된다.

- 생산자가 동시에 데이터를 불러가면 안된다.

Producer는 공유 데이터에 데이터를 입력하는 역활

- Empty 버퍼가 있을 때 까지 기다림

- 공유데이터에 lock를 건다

- Empty Buffer에 데이터 입력 및 Buffer 조작

- Lock을 푼다

- Full Buffer 하나 증가

Consumer는 버퍼에 있는 데이터를 읽어가는 역활

- Full 버퍼가 있을 때 까지 기다림

- 공유데이터에 lock를 건다.

- Full Buffer에서 데이터를 꺼내고 Buffer 조작

- Lock을 푼다.

- Empty Buffer 하나 증가

#### Readers - Writers Problem

한 Process가 DB에 Write 중일 때 다른 Process가 접근하면 안됨

Read는 동시에 여럿이 해도 됨

Solution

- Writer가 DB에 접근 허가를 하직 얻지 못한 상태에서는 모든 대기중인 Reader들을 다 DB에 접근하게 해준다.

- Writer는 대기 중인 Reader가 하나도 없을 때 DB 접근이 허용된다.

- 일단 Writer가 DB에 접근 중이면 Reader들은 접근이 금지된다.

- Writer가 DB에서 빠져나가야만 Reader의 접근이 허용된다.

Shared Data

- DB 자체

- Readcount ( 현재 DB에 접근 중인 Reader의 수)

Synchronization variables

- Mutex ( 공윤 변수 readcount를 접근하는 코드 (critical section)의 mutual exclusion을 보장을 위해 사용)

- DB (Reader와 Writer가 공유 DB 자체를 올바르게 접근하게 하는 역할)

#### Dining Philosophers Problem

대표적인 교착상태 (Dead Lock) 문제

Synschronization Variables

Semaphore Chopstick[5];
( 모두 1로 초기화)

```c
do {
  P(chopstick[i]);
  P(chopstick[(i+1) %5]);

  eat()

  V(chopstick[i]);
  V(chopstick[(i+1) %5]);

  think();
}while(1);
```

문제점

- Deadlock 가능성이 있다.

- 모든 철학자가 동시에 배가 고파져 왼쪽 젓가락을 집어버린 경우

해결 방안

- 4명의 철학자만이 테이블에 동시에 앉을 수 있도록 한다.

- 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다.

- 비대칭 : 짝수 철학자는 왼쪽 젓가락부터 잡도록 한다.

---

### Monitor

동시 수행중인 프로세스 사이에서 추상화 데이터 타입의 안전한 공유를 보장하기 위한 high-level synchronization constructor이다.

Semaphore의 문제점

- 코딩하기 힘들다.

- 정확성의 입증이 어렵다.

- 자발적 협력이 필요하다.

- 한번의 실수가 모든 시스템에 치명적 영향을 준다.

모니터 내에서는 한번에 하나의 프로세스만이 활동 가능

프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요없음

프로세스가 모니터 안에서 기다릴 수 있도록 하기 위해 Condition variable 사용

condition variable은 wait와 signal 연산에 의해서만 접근 가능

wait()

- x.wait()을 invoke한 프로세스는 다른 프로세스가 x.signal()을 invoke하기 전까지 suspend된다.

singal()

- x.signal()은 정확하게 하나의 suspend된 프로세스를 resume한다. suspend된 프로세스가 없으면 아무 일도 일어나지 않는다.
