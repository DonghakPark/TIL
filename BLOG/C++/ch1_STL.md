### STL이란 무엇인가 ?

- 표준 C++ 라이브러리를 뜻한다. (Standard Template Library)
- C++ 언어로 프로그래밍 하는데 필요한 자료구조와 알고리즘을 제공하는 라이브러리 이다.

### STL의 구성 요소

- Container
  - 객체를 저장하는 객체, 자료구조 등으로 클래스 템플릿으로 구현되어 있다.
  - ex) array, vector, list, deque, set, multiset, map, multimap
- Iterator
  - 포인터와 유사한 개념으로 컨테이너의 원소를 가리키고, 접근한다. 다음 워소를 가리키는 기능, 순회 등을 수행할 수 있다.
- Algorithm
  - 정렬, 삭제, 검색, 연산 등을 해결하는 일반화된 방법을 제공
- Function Object
  - 함수처럼 동작하는 객체
  - 컨테이너와 알고리즘 등에 클라이언트 정책을 반영하게 함
- Contanier Adaptor
  - 구성 요소의 인터페이스를 변경, 새로운 인터페이스를 갖는 구성요소로 변겨
  - ex) Stack, Queue, Priority Queue
- Allocator
  - 컨테이너의 메모리 할당 정책을 캡슐화한 클랙스 객체로 모든 컨테이너는 자신만의 할당기를 가지고 있다.

### STL의 장점

- 일반화를 지원한다.
- 컴파일 타임 매커니즘을 사용하므로, 효율 저하에 견고하다.
- 표준으므로 이식성, 협업에 유리하다.
- 확장이 가능하다.

### STL의 단점

- 타입 별로 함수, 클래스가 구체화되어 코드의 양이 많아진다.
- 가독성이 떨어진다.

##### Reference

1. https://blockdmask.tistory.com/67?category=249379
2. https://codingplus.tistory.com/13?category=704484
