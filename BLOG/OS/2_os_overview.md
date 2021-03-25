운영체제가 다루는 영역은 광범위하다. 현대 시스템에 있어 컴퓨터는 멀티 코어, 멀티 쓰레드 환경을 구축하고 있고 이에 따라 다양한 요구사항들이 반영되었기 때문이다. 아래에는 운영체제를 올바르게 이해하기 위한 요소들을 설명할 것이다.

#### 프로그램이 실행될 때 어떤 일들이 일어나는가 ?

1. 논리적 관점
   - 컴퓨터는 크게 CPU, Memory, I/O로 이루어져 있다 프로그램이 실행 될때 이 세가지 요소는 다음과 같은 일을 수행한다.
     - CPU : 연산 처리
     - I/O : 입출력
     - Memory : 명령어와 데이터 저장
   - 이러한 요소들 간의 통신은 System Bus를 통해서 이루어 진다.
   - 즉 논리적 관점에서 보자면 프로그램이 실행된다는 것은 데이터와 명령어가 CPU로 이동하여 실행된다는 것이다.
2. 명령어 실행
   - 명령어가 실행된다는 것은 Fetch Instruction, Execute Instruction이 반복 된다는 것이다. CPU는 명령어 셋을 가지고 있고 이러한 명령어 셋은 사전에 정의되어 특정한 작업을 수행할 수 있다. (ex. 더하기 연산, 곱하기 연산 등) 이러한 명령어가 전달되고 필요로 하는 데이터 또한 전송되면 이를 실행하여 결과를 반환하는 것이 실제 CPU가 수행하는 작업니다.
   - 이러한 작업은 굉장히 빠른 속도로 수행되며, 작업들이 모여 우리가 보는 프로그램이 작동되는 것이다.
3. 프로그램을 실행하기 위한 많은 작업들
   - 이런 단순한 동작이 우리 눈에 보이는 프로그램이 되기에는 많은 부수적인 작업들이 필요하다.
   - Loading, Memory Magement, Scheduling, Context Switching, I/O processing, File Management, IPC 등이 그 예시이다.

#### 즉 이러한 복잡한 작업들을 사용자로 사여금 더욱 쉽고, 올바르고, 효율적으로 작동하게 하는 것이 운영체제가 하는 일이다.

- 운영체제는 다음과 같은 역활을 맡고 있다고 할 수 있다.

1. Resource Manager
   - Physical Resources : CPU, DRAM, Disk, Flash, KBD, Network, .....
   - Virtual Resources : Process, Thread, Virtual Memory, Page, File, Directory, Driver, Protocol, Access control, Security
2. Virtualization (Abstraction)
   - 물리적인 자원을 보다 쉽고, 강하게 사용할 수 있도록 추상화
3. System Call 제공
   - 시스템콜은 운영체제에 의해 제공되는 API라고 할 수 있다.
   - Unix에서 제공되는 fork(), exit(), wait(), open()과 같은 명령어들이 이와 같다.
   - 이러한 시스템 콜은 User Mode -> Kernel Mode로의 Mode Switch를 제공한다.

### Virtualizing CPU

<!-- 다음은 앞으로의 설명을 위한 예제 코드이다.
```{.C}
// This Code From OSTEP

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <assert.h>
#include "common.h"

int main(int argc, char *argv[]){
    if (argc != 2){
        fprintf(stderr, "usage : cpu <string>\n");
        exit(1);
    }
    char *str = argv[1];
    while(1){
        Spin(1);
        printf("%s\n",str);
    }
    return 0;
}
```
이 코드의 기능은 입력된 데이터를 반복적으로 출력하는 것이다. -->

- Issues for Virtualizing CPU
  - How to run a new program : process
  - How to make a new process : fork()
  - How to stop a process? : exit()
  - How to execute a new process? : exec()
  - How to block a process : sleep(), pause(), lock(), ....
  - How to select a process to run next? : Scheduling
  - How to run multiple processes ? : Context Switch
  - How to manage Multiple cores (CPUs) : multi-processor scheduling, cache affinity, load balancing
  - How to Communicate among processes : IPC (inter process communication), socket
  - How to notify an event to a process : signal
