## Process Management(프로세스 관리)

---

### 프로세스 생성( Process Creation )

부모 프로세스가 자식 프로세스 생성

프로세스의 트리(계층 구조) 형성

프로세스는 자원을 필요로 함

- 운영체제로부터 받는다.

- 부모와 공유한다.

자원의 공유

- 부모와 자식이 모든 자원을

공유하는 모델

- 일부를 공유하는 모델

- 전형 공유하지 않는 모델

수행 (Execution)

- 부모와 자식은 공존하며

수행되는 모뎅

- 자식이 종료(Terminate)될 때까지 부모가 기다리는(Wait) 모델

주소 공간 (Address Space)

- 자식은 부모의 공간을 복사함 (binary and OS data)

- 자식은 그 공간에 새로운 프로그램을 올림

유닉스 예

- fork() 시스템 콜이 새로운 프로세스를 생성

  - 부모를 그대로 복사 (OS data except PID + binary) -> 문맥을 복사한다고 볼 수 있다.

  - 주소 공간 할당

- fork 다음에 이어지는 exec() 시스템 콜을 통해 새로운 프로그램을 메모리에 올리

---

### 프로세스 종료 (Process Termination)

프로세스가 마지막 명령을 수행한 후 운영체제에게 이를 알려줌 (Exit)

- 자식이 부모에게 Output data를 보냄 (wait)
- 프로세스의 각종 자원들이 운영체제에게 반납됨

부모 프로세스가 자식의 수행을 종료시킴 (abort)

- 자식이 할당 자원의 한계치를 넘어섬

- 자식에게 할당된 테스크가 더 이상 필요하지 않음

- 부모가 종료하는 경우

  - 운영체제는 부모 프로세스가 종료하는 경우 자식이 더 이상 수행되도록 두지 않는다.

  - 단계적인 종료

COW(copy on write) 기법을 활용하기도 함 : Write가 발생했을 때 Copy를 수행하겠다.

---

### fork() 시스템 콜

A process is created by the fork() system call

- creates a new address space that is a duplicate of the caller

```c
int main()
{
    int pid;
    pid = fork();
    if (pid == 0){
        printf("\n Hello, i am child!\n");
    }
    else if (pid>0){
        printf("\m Hello, i am parent!\n");
    }
}
```

이때 자식과 부모 프로세스를 구별하기 위해 return 값이 다르다 이를 통해서 자식과 부모를 구별하여 별도의 작업을 시킬 수 있다.

- 부모 프로세스 : 자식의 pid (양수)

- 자식 프로세스 : 0

---

### exec() System Call

A process can execute a different program by the exec() system call

- replaces the memory image of the caller with a new program

```c
int main(){
    int pid;
    pud = fork();
    if (pid == 0){
        printf("\n Hello, i am child! Now i'll run date \n");
        execlp("/bin/date", "/bin/date", (char*) 0);
        /*
        exec()을 실행할 경우 새로운 프로그램의 main 부터 다시 시작한다.
        */
    }
    else if (pid > 0 ){
        printf("\n Hello, i am parent!\n");
    }
}
```

---

### wait() System Call

프로세스 A가 wait() 시스템 콜을 호출하면

- 커널은 child가 종료될 때까지 프로세스 A를 sleep시킨다. (block 상태)

- child process가 종료되면 커널은 프로세스 A를 꺠운다. (ready 상태)

```c
int main(){
    int childPID;

    childPID = fork();
    if (childPID == 0){
        // ~~~
    }
    else{
        wait(); //자식 프로세스가 끝날 때까지 대기
    }

}
```

---

### exit() System Call

프로세스의 종료

- 자발적 종료

  - 마지막 statement 수행 후 exit() 시스템 콜을 통해

  - 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌

- 비자발적 종료

  - 부모 프로세스가 자식 프로세스를 강제 종료시킴

    - 자식 프로스세가 한계치를 넘어서는 자원 요청

    - 자식에게 할당된 테스크가 더 이상 필요하지 않음

  - 키보드로 kill, break 등을 친 경우

  - 부모가 종료하는 경우

    - 무보 프로세스가 종료하기 전에 자식들이 먼저 종료됨

---

#### 프로세스와 관련한 시스템 콜

fork() : create a child

exec() : overlay new image

wait() : sleep until child is done

exit() : frees all the resources, notify parent

---

### 프로세스 간 협력

독립적 프로세스 (Independent process)

- 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함

협력 프로세스 (Cooperating Process)

- 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음

프로세스 간 협력 메커니즘 (IPC : Interprocess Communication)

- 메시지를 전달하는 방법

  - message passing : 커널을 통해 메세지를 전달

- 주소 공간을 공유하는 방법

  - shared memory : 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 shared memory 매커니즘이 있음

  - thread : thread는 사실상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 process를 구성하는 thread 간에는 주소 공간을 공유하므로 협력이 가능

---

### Message Passing

message system

- 프로세스 사이에 공유 변수를 일체 사용하지 않고 통신하는 시스템

Direct Communication

- 통신하려는 프로세스의 이름을 명시적으로 표시

Indirect Communication

- mailbox or port를 통해 메시지를 간접 전달
