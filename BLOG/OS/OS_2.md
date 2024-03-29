## System Structure & Program Execution (컴퓨터 시스템과 프로그램의 실행)

> ### CPU의 역활
>
> CPU는 매순간 메모리의 있는 기계어를 읽어와 실행을 하게된다.

- Program Counter가 가르키고 있는 다음 명령어를 로딩한다.
- 특별한 일이 없으면 CPU는 다음 명령어를 수행한다.
- 제어문이나 특별한 명령어를 만나면 점프를 하거나, 반복한다.
- 즉 CPU는 아주 빠른 일꾼이라고 생각하면 된다.

> ### mode bit

mode bit이 0이냐 1이냐에 따라서

- 0이면 CPU가 실행가능한 모든 명령어 실행 가능
- 1이면 한정된 명령어만 수행가능

- 0 : 운영체제가 가지고 있음
- 1 : 사용자 프로그램이 CPU를 가지고 있음 > 사용자 프로그램을 100프로 믿을 수 없기 때문에, 자기 메모리 주소영역만 볼 수 있게함

I/O 디바이스를 접근하는 mode bit 이 0일때만 사용가능

따라서 사용자 프로그래밍 운영체제에 서비스를 요청할 때는 시스템 콜을 사용

사용자 프로그램이 I/O를 사용하는 방법

시스템콜(System Call)

- 사용자 프로그램은 운영체제에게 I/O 요청
- Trap을 사용하여 인터럽트 벡터의 특정 위치로 이동
- 제어권이 인터럽트 벡터가 가리키는 인터럽트 서비스 루틴으로 이동
- 올바른 I/O 요청인지 확인 후 I/O 수행
- I/O 완료 시 제어권을 시스템콜 다음 명령으로 옮김

> ### 인터럽트

인터럽트 당한 시점의 레지스터와 Program Counter를 Save한 후 CPU의 제어를 인터럽트 처리 루틴에 넘긴다.

하드웨어 인터럽트 : 하드웨어가 발생시킨 인터럽트
소프트웨어 인터럽트 (Trap)

Exception : 예외처리 (프로그램 오류 발생)
System Call : 프로그램이 커널 함수를 호출하는 경우

인터럽트 벡터

- 해당 인터럽트의 처리 루틴 주소를 가지고 있음

인터럽트 처리 루틴 (Interrupt Service Routine, Interrupt Handler)

- 해당 인터럽트를 처리하는 커널 함수

> #### Timer

사용자 프로그램이 CPU를 무한히 사용하는 것 같은 상황을 대비
일정 시간이 지나면 CPU의 제어권을 OS로 돌려줌
여러 프로그램을 문제 없이 실행 할 수 있음

> ### 동기식 입출력과 비동기식 입출력

동기식 입출력 (Synchronous I/O)

I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감

- ex) I/O가 끝날 때까지 대기, 매시점 하나의 I/O만 일어남

비동기식 입출력 (Asynchronous I/O)

- I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에게 넘어감

두 경우 모두 I/O의 완료는 인터럽트로 알려준다.

> ### DMA (Direct Memory Access) Controller

모든 인터럽트에 따라 메모리에 접근하게 되면 CPU 작업에 오버헤드가 너무 많이 발생한다.

- 따라서 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
- CPU의 중재 없이 Device Controller가 Device의 Buffer Storage의 내용을 메모리에 Block 단위로 직접 전송
- 바이트가 아닌 Block 단위로 인터럽트를 발생
- 성능 향상을 기대할 수 있음

> ### Program Excution

파일 시스템의 프로그램이 메모리에 올라가서 실행되면 프로세스가 된다.

이때 프로세스별로 독자적인 주소공간을 확보하기 위해서 가상 메모리(Virtual Memory)라는 개념(논리적인 개념)이 사용된다.

가상 메모리 공간은 코드, 데이터, 스택, 힙으로 이루어진다.

이러한 가상메모리는 물리적인 메모리에 로드되는데, 이때 사용되는 부분만 로드하여 메모리 공간의 낭비를 막는다. 하지만 보관되어야 하는 부분은 스왑(Swap) 영역에 내려놓게 된다.

> ### 사용자 프로그램이 사용하는 함수

사용자 정의 함수 : 프로세스의 code 영역

- 사용자가 직접 작성, 정의한 함수

라이브러리 함수 : 프로세스의 code 영역

- 다른 사람이 만들어 놓은 유용한 기능

Kernel 함수 : Kernel의 Code 영역

- 운영체제 안에서 정의된 함수
- 커널 함수의 호출 : 시스템 콜

Reference
: KOCW 반효경 교수님의 운영체제 수업
