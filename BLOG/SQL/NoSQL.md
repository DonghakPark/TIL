### NoSQL 데이터베이스란 ?

- NoSQl 데이터베이스는 특정 데이터 모델에 대해 특정 목적에 맞추어 구축되는 데이터베이스로서 현대적인 어플리케이션 구축을 위한 유연한 스키마를 가진 것이 특징입니다.
- NoSQL 데이터베이스는 개발의 용이성, 기능성 및 확장성을 널리 인정받고 있습니다.

#### NoSQL의 특징

- ACID (Atomic, Consistency, Integrity, Duarabity)특성을 제공하지 않지만, 뛰어난 확장성이나 성능을 제공함
- 비정형 데이터를 보다 쉽게 담아서 저장하고 처리할 수 있는 구조를 가진 DB가 필요해지면서 점점 발전되어감
- 관계형 모델을 사용하지 않으며 테이블 간 연결해서 조회할 수 있는 조인 기능이 없음
- 데이터 조회를 위해 직접 프로그래밍하는 등의 비 SQL 인터페이스를 통한 데이터 접근
- 대부분 여러 데이터베이스 서버를 묶어서 하나의 데이터베이스를 구성
- 관계형 데이터베이스에서는 지원하는 데이터 처리 완결성 (Transaction, ACID)이 보장되지 않음
- 데이터 스키마와 속성들을 다양하게 수용하고 동적으로 정의(Schemaless)
- 데이터베이스의 중단없는 서비스와 자동 복구 기능 지원
- 대다수의 제품이 Open Source로 제공
- 대다수의 제품이 고 확장성, 고 가용성, 고 성능 특징을 가짐

#### NoSQL의 종류

- Key-value DB : Key와 Value 쌍으로 데이터가 저장되는 유형으로써 Amazon의 Dynamo Paper에서 유래
- Wide Columnar DB : Big Table DB라고도 부르며, Column Family 데이터 모델을 사용하고 있음
- Document DB : Json, XML과 같은 Collection 데이터 모델 구조를 채택함 -> Mongo DB, Cough DB가 해당
- Graph DB : Nodes, Relationship, Key-Value 데이터 모델을 채용하고 있음
