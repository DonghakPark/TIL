> 본 게시물은 KOCW의 반효경 교수님의 강의를 기반으로 정리한 것입니다.

## Deadlock (교착상태)

Deadlock : 일련의 프로세스들이 서로가 가진 자원을 기다리며 block된 상태

Resource (자원)

- 하드웨어, 소프트웨어 등을 포함하는 개념

- 프로세스가 자원을 사용하는 절차 : Request, Allocate, Use, Release

---

### Deadlock 발생의 4가지 조건

Mutual Exclusion (상호배제)

- 매 순간 하나의 프로세스만이 자원을 사용할 수 있음

No Preemption (비선점)

- 프로세스는 자원을 스스로 내어놓을 뿐 강제로 빼앗기지 않음

Hold and Wait (점유대기)

- 자원을 가진 프로세스가 다른 자원을 기다릴 때 보유 자원을 놓지 않고 계속 가지고 있음

Circular Wait (환형 대기, 순환 대기)

- 자원을 기다리는 프로세스간에 사이클이 형성되어야함

교착상태를 알아보기 위해서 "자원할당그래프"를 그려서 알아보기도 한다.

자원 할당 그래프에서 cycle이 없으면 데드락이 아니다.

만약 사이클이 있으면

- 자원당 인스턴스가 남지 않는다면 데드락이다.

- 여러 자원이 있다면 데드락일 수도 있고 아닐 수도 있다.

---

### Deadlock 처리 방법

Deadlock Prevention

- 자원 할당 시 Deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 하는 것

Deadlock Avoidance

- 자원 요청에 대한 부가적인 정보를 이용해서 deadlock의 가능성이 없는 경우에만 자원을 할당

- 시스템 state가 원래 state로 돌아올 수 있는 경우에만 자원 할당

Deadlock Detection and Recovery

- Deadlcok 발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견시 recover

Deadlock Ignorance

- Deadlock을 시스템이 책임지지 않음

- UNIX를 포함한 대부분의 OS가 채택

---

### Deadlock Prevention

Mutual Exclusion

- 공유해서는 안되는 자원의 경우 반드시 성립해야 함

Hold and Wait

- 프로세스가 자원을 요청할 때 다른 어떤 자원도 가지고 있지 않아야 한다.

  - 방법 1. 프로세스 시작 시 모든 필요한 자원을 할당 받게하는 방법

  - 방법 2. 자원이 필요한 경우 보유 자원을 모두 놓고 다시 요청

No Preemption

- Process가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨

- 모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작된다.

- State를 쉽게 Save하고 restore할 수 있는 자원에서 주로 사용

Circular wait

- 모든 자원 유형에 할당 순서를 정하여 정해진 순서대로만 자원 할당

-----> 이러한 방법은 Utilization을 저하하고, Throughput을 감소시키면 Starvation문제를 야기할 수 있다.

---

### Deadlock avoidance

자원 요청에 대한 부가정보를 이용해서 자원 할당이 Deadlock으로 부터 안전한지를 동적으로 조사해서 안전한 경우에만 할당

가장 단순하고 일반적인 모델은 프로세스들이 필요로 하는 각 자원별 최대 사용량을 미리 선언하도록 하는 방법임

safe state

- 시스템 내의 프로세스들에 대한 safe sequence가 존재하는 상태

safe sequence

- 프로세스의 sequence이 safe하려면 프로세스의 자원 요칭이 " 가용 자원 + 모든 프로세스들의 보유 자원"에 의해 충족되어야 함

- 조건을 만족하기 위해 다음 방법으로 모든 프로세스들의 수행을 보장

  - A 프로세스의 자원 요청이 즉시 충족될 수 없으면 모든 이전 프로세스가 종료될 때까지 기다린다.

  - 직전 프로세스의 수행이 종료되면 프로세스의 자원요청을 만족시켜 수행한다.

single instance per resource types : Resource Allocation Graph Alogorithm 사용

multiple instances per resource types : Banker's Algorithm 사용

#### Banker's Algorithm

가정

- 모든 프로세스는 자원의 최대 사용량을 미리 명시

- 프로세스가 요청 자원을 모두 할당받은 경우 유한 시간 안에 이들 자원을 다시 반납한다.

방법

- 기본 개념 : 자원 요청시 safe 상태를 유지할 경우에만 할당

- 총 요청 자원의 수가 가용 자원의 수보다 적은 프로세스를 선택

- 그런 프로세스가 있으면 그 프로세스에게 자원을 할당

- 할당받은 프로세스가 종료되면 모든 자원을 반납

- 모든 프로세스가 종료될 때까지 이러한 과정 반복

--> 최악의 상황을 가정해서 남는 자원을 할당하지 않기 때문에 비효율적이라고 볼 수 있다.

---

### Deadlock Detection and Recovery

Deadlock Detection

- Resource type 당 single instance인 경우

  - 자원 할당 그래츠에서의 cycle이 곧 deadlock을 의미

- Resource type 당 multiple instance인 경우

  - Banker's Algorithm과 유사한 방법 활용

Wait for graph 알고리즘

Resource type 당 single instance인 경우

wait for graph

- 자원할당 그래프의 변형

- 프로세스만으로 node 구성

Algorithm

- Wait for graph에 사이클이 존재하는지를 주기적으로 조사

- O(n^2)만큼의 시간 복잡도를 가짐

Recovery

- Process termination

  - abort all deadlocked processes

  - abort one process at a time until the deadlock cycle is eliminated

- resource Preemption

  - 비용을 최소화할 victim의 선정

  - safe state로 rollback하여 process를 restart

  - starvation 문제

    - 동일한 프로세스가 계속해서 victim으로 선정되는 경우

    - cost factor에 rollback 횟수도 같이 고려

---

### Deadlock Ignorance

deadlock이 일어나지 않는다고 생각하고 아무런 조치도 취하지 않는다.

- 데드락이 매우 드물게 발생하므로 조치를 취하지 않는다.

- 데드락이 발생한 경우 사용자가 직접 다루도록 한다.

- Unix, window등 현재 대부분의 시스템이 이러한 방식을 채택하고 있음

- 데드락을 처리하는 오버헤드가 크기 때문
