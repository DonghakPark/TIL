> 본 게시물은 KOCW의 반효경 교수님의 강의를 기반으로 정리한 것입니다.

### Memory Management (메모리 관리)

---

### Logical vs Physical Address

Logical Address (Virtual Address)

- 프로세스마다 독립적으로 가지는 주소 공간

- 각 프로세스마다 0번지부터 시작

- CPU가 보는 주소는 Logical Address

Physical Address

- 메모리에 실제 올라가는 위치

주소 바인딩 : 주소를 결정하는 것

- Symbolic Address --> Logical Address --> Physical Address

---

### 주소 바인딩 (Address Binding)

Compile time binding

- 물리적 메모리 주소가 컴파일 시 알려짐

- 시작 위치 변경시 재컴파일

- 컴파일러는 절대 코드 생성

Load time binding

- loader의 책임하에 물리적 메모리 주소 부여

- 컴파일러가 재배치가능 코드 (relocatable code)를 생성한 경우 가능

Execution time binding (Run Time Binding)

- 수행이 시작된 이후에도 프로세스의 메모리 상 위치를 옮길 수 있음

- CPU가 주소를 참조할 때마다 Binding을 점검 (Address Mapping Table)

- 하드웨어적인 지원이 필요

![image](https://user-images.githubusercontent.com/44962038/119782567-4d732480-bf07-11eb-9d9f-dd83c2fd9277.png)_KOCW 강의 자료에서 가져온 사진입니다._

---

### Memory Management Unit (MMU)

MMU (Memory Management Unit)

- Logical address를 Physical Address로 매핑해 주는 Hardware device

MMU Scheme

- 사용자 프로세스가 CPU에서 수행되며 생성해주는 모든 주소값에 대해 Base Register (= Relocation Register)의 값을 더한다.

User Program

- Logical Address만을 다룬다.

- 실제 Physical Address를 볼 수 없으며 알 필요가 없다.

#### Hardware Support for Address Translation

운영체제 및 사용자 프로세스 간의 메모리 보호를 위해 사용하는 레지스터

- Relocation Register (Base Register) : 접근할 수 있는 물리적 메모리 주소의 최소값

- Limit Register : 논리적 주소의 범위

---

### 용어 정리

#### Dynamic Loading

프로제스 전체를 메모리에 미리 다 올리는 것이 아니라 해당 루틴이 불려질 때 메모리에 load하는 것

Memory Utilization의 향상

가끔씩 사용되는 많은 양의 코드의 경우 유용

운영체제의 특별한 지원 없이 프로그램 자체에서 구현 가능 (OS는 라이브러리를 통해 지원 가능)

Loading은 메모리에 데이터를 올리는 것을 의미함, 여기서 말하는 Dynamic Loading은 운영체제가 하는 것이 아닌 프로그래머가 진행하는 것을 말함.

--> 직접 모든 것을 다루는 것이 아니라 라이브러리를 활용해서 작성함

#### Overlays

메모리에 프로세스의 부분 중 실제 필요한 정보만을 올림

프로세스의 크기가 메모리보다 클 때 유용

운영체제의 지원없이 사용자에 의해 구현

작은 공간의 메모리를 사용하던 초창기 시스템에서 수작업으로 프로그래머가 구현

--> 예전에 메모리의 크기가 작을 때 사용되던 방법 : Dynamic Loading이랑은 그런 부분에서 다름

#### Swapping

Swapping

- 프로세스를 일시적으로 메모리에서 Backing Store로 쫓아내는 것

Backing Store (Swap area)

- 디스크 : 많은 사용자의 프로세스 이미지를 담을 만큼 충분히 빠르고 큰 저장 공간

Swap in / Swap out

- 일반적으로 중기 스케쥴러에 의해 swap out 시킬 프로세스 선정

- Priority based CPU scheduling Algorithm

  - 우선순위가 낮은 프로세스를 swapped out 시킴

  - 우선순위가 높은 프로세스를 메모리에 올려 놓음

- Compile Time 혹은 Load time binding에서는 원래 메모리 위치로 swap in 해야 함

- Execution time binding에서는 추후 빈 메모리 영역 아무 곳에나 올릴 수 있음

- Swap Time은 대부분 Transfer time (swap 되는 양에 비례하는 시간)임

### Dynamic Linking

Linking을 실행 시간 (Execution Time)까지 미루는 기법

Static Linking

- 라이브러리가 프로그램의 실행 파일 코드에 포함됨

- 실행 파일의 크기가 커짐

- 동일한 라이브러르를 각각의 프로세스가 메모리에 올리므로 메모리 낭비

Dynamic Linking

- 라이브러리가 실행시 연결됨

- 라이브러리 호출 부분에 라이브러리 루틴의 위치를 찾기 위한 stub이라는 작은 코드를 둠

- 라이브러리가 이미 메모리에 있으면 그 루틴의 주소로 가고 없으면 디스크에서 읽어옴

- 운영체제의 도움이 필요

---

### Allocation of Physical Memory

메모리는 일반적으로 두 영역으로 나뉘어 사용

- OS 상주 영역 : Interrupt Vector와 함께 낮은 주소 영역 사용

- 사용자 프로세스 영역 : 높은 주소 영역 사용

사용자 프로세스 영역의 할당 방법

- Contiguous allocation

  - 각각의 프로세스가 메모리의 연속적인 공간에 적재되도록 하는 것

  - Fixed Partition Allocation

  - Variable Partition Allocation

- Noncontiguous allocation

  - 하나의 프로세스가 메모리의 여러 영역에 분산되어 올라갈 수 있음

  - Paging

  - Segmentation

  - Paged Segmentation

---

### Contiguous Allocation

고정 분할 방식

- 물리적 메모리를 몇 개의 영구적 분할로 나눔

- 분할의 크기가 모두 동일한 방식과 서로 다른 방식이 존재

- 분할당 하나의 프로그램 적재

- 융통성이 없음

  - 동시에 메모리에 load되는 프로그램의 수가 고정된

  - 최대 수행 가능 프로그램 크기 제한

- Internal Fragmentation 발생 (External Fragmentation도 발생)

가변 분할 방식

- 프로그램의 크기를 고려해서 할당

- 분할의 크기, 개수가 동적으로 할당

- 기술적 관리 기법 필요

- External Fragmentation 발생

Hole

- 가용 메모리 공간

- 다양한 크기의 hole들이 메모리 여러 곳에 흩어져 있음

- 프로세스가 도착하면 수용가능한 hole을 할당

- 프로세스가 도착하면 수용가능한 hole을 할당

- 운영체제는 다음의 정보를 유지

  - 할당 공간

  - 가용 공간 (Hole)

#### Dynamic Storage Allocation Problem

가변 분할 방식에서 Size n인 요청을 만족하는 가장 적절한 hole을 찾는 문제

First - fit

- Size가 n이상인 것 중 최초로 찾아지는 hole에 할당

Best - fit

- Size가 n 이상인 가장 작은 hole을 찾아서 할당

- Hole들의 리스트가 크기순으로 정렬되지 않은 경우 모든 hole의 리스트를 탐색해야함

- 많은 수의 아주 작은 hole들이 생성됨

Worst - fit

- 가장 큰 hole에 할당

- 역시 모든 리스트를 탐색해야 함

- 상대적으로 아주 큰 hole들이 생성됨

실험적으로 first-fit이나 best-fit이 worst-fit보다 속도와 공간 이용을 측면에서 효과적인 것으로 알려짐

Compaction

- External Fragmentation 문제를 해결하는 한가지 방법

- 사용 중인 메모리 영역을 한군데로 몰고 hole들을 다른 한 곳으로 몰아 큰 block을 만드는 것

- 매우 비용이 많이 드는 방법임

- 최소한의 메모리 이동으로 compaction하는 방법

- Compaction은 프로세스의 주소가 실행 시간에 동적으로 재배치 가능한 경우에만 실시할 수 있다.

---

### Paging

Paging

- Process의 Virtual Memory를 동일한 사이즈의 pahe 단위로 나눔

- Virtual Memory의 내용이 Page 단위로 noncontiguous하게 저장됨

- 일부는 backing Storage에 일부는 physical memory에 저장

Basic Method

- 물리 주소를 동일한 크기의 프레임으로 나눔

- 논리 메모리를 동일 크기의 페이지로 나눔

- 모든 가용 프레임들을 관리

- 페이지 테이블을 사용하여 논리주소를 물리주소로 변환

- 외부 단편화 발생 안함

- 내부 단편화 발생 가능

#### Implementation of Page Table

page table은 main memory에 상주

Page Table Base Register (PTBR)가 Page Table을 가리킨

Page Table Length Register (PTLR)가 테이블 크기를 보관

모든 메모리 접근 연산에는 2번의 memory access 필요

Page Table 접근 1번 + 실제 data/Instruction 접근 1번

속도 향상을 위해 associative register 혹은 translation lock aside buffer (TLB)라 불리는 고속의 lookup hardware cache 사용

#### Associative Register

Associative registers (TLB) : parallel search가 가능

- TLB에는 page Table 중 일부만 존재

Address Translation

- page table 중 일부가 associative register에 보관되어 있음

- 만약 해당 page num가 associative register에 있는 경우 곧바로 frame num을 얻음

- 그렇지 않은 경우 main memory에 있는 page table로 부터 frame num을 얻음

- TLB는 context switch 때 flush (remove old entries)

#### Effective Access Time

Associative register lookup time = e

memory cycle time = 1

Hit ratio = a (associative register에서 찾아지는 비율)

Effective Access Time = (1 + e)a + (2 + e)(1 - a)

---> 2 + e - a

---

### 2 Level page table

page table을 위한 공간을 줄이기 위해 사용

현대의 컴퓨터는 address space가 매우 큰 프로그램을 지원

- 32 bit addesss 사용시 ==> 4GB의 주소 공간

  - Page Size가 4K시 1M개의 page table entry가 필요

  - 각 page entry가 4B시 프로세스당 4M의 page table 필요

  - 그러나 대부분의 프로그램은 4G의 주소 공간 중 지극히 일부분만 사용하기 때문에 낭비가 심함

- 페이지 테이블 자체를 페이지로 구성

- 사용되지 않는 주소 공간에 대한 outer page table의 엔트리 값은 NULL (대응하는 inner page table이 없음)
