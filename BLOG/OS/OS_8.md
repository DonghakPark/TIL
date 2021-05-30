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
