## SQL 응용

### SQL의 개념

1. SQL(Structured Query Language)의 개요
   - 국제 표준 데이터베이스 언어이며, 많은 회사에서 관계형 데이터베이스를 지원하는 언어로 체택한다.
   - 관계대수와 관계해석을 기초로 한 혼합 데이터 언어이다.
   - 질의어지만 질의 기능만 있는 것이 아니라 데이터 구조의 정의, 데이터 조작, 데이터 제어 기능을 모두 갖추고 있다.
2. SQL의 분류
   - DDL : 데이터 정의어
     - SCHEMA, DOMAIN, TABLE, VIEW, INDEX를 정의하거나 변경 또는 삭제할 때 사용하는 언어이다.
     - 논리적 데이터 구조와 물리적 데이터 구조의 사상을 정의한다.
     - 데이터 베이스 관리자나 데이터 베이스 설계자가 사용한다.
     - CREATE : SCHEMA, DOMAIN, TABLE, VIEW, INDEX를 정의한다.
     - ALTER : TABLE에 대한 정의를 변경하는데 사용한다.
     - DROP : SCHEMA, DOMAIN, TABLE, VIEW, INDEX를 삭제한다.
   - DML : 데이터 조작어
     - DML은 데이터베이스 사용자가 응용 프로그램이나 질의어를 통하여 저장된 데이터를 실질적으로 체리하는 데 사용되는 언어이다.
     - 데이터베이스 사용자와 데이터베이스 관리 시스템 간의 인터페이스를 제공한다.
     - SELECT : 테이블 조건에 맞는 튜플을 검색한다.
     - INSERT : 테이블에 새로운 튜플을 삽입한다.
     - DELETE : 테이블에서 조건에 맞는 튜플을 삭제한다.
     - UPDATE : 테이블에서 조건에 맞는 튜플의 내용을 변경한다.
   - DCL : 데이터제어어
     - DCL은 데이터의 보안, 무결성, 회복, 병행 수행 제어 등을 정의하는데 사용되는 언어이다.
       - 데이터베이스 관리자가 데이터 관리를 목적으로 사용한다.
       - COMMIT : 명령에 의해 수행된 결과를 실제 물리적 디스크에 저장하고, 데이터베이스 조작 작업이 정상적으로 완료되었음을 관리자에게 알려준다.
       - ROLLBACK : 데이터베이스 조작 작업이 비정상적으로 종료되었을 때 원래의 상태로 복구한다.
       - GRANT : 데이터베이스 사용자에게 사용권한을 부여한다.
       - REVOKE : 데이터베이스 사용자의 사용 권한을 취고한다.

### DDL

1. DDL의 개념
   - DDL의 DB구조, 데이터 형식, 접근 방식 등 DB를 구축하거나 수정할 목적으로 사용하는 언어이다.
2. CREATE SCHEMA
   - 스키마를 정의하는 명령문이다.
   ```{.sql}
   CREATE SCHEMA sample AUTHORIZATION sampel_user;
   ```
3. CREATE DOMAIN
   - 도메인을 정의하는 명령문
   ```{.sql}
   CREATE DOMAIN SEX CHAR(1)
       DEFAULT "남"
       CONSTRAINT VALID-SEX CHECK(VALUE IN('남','여'));
   ```
4. CREATE TALBE
   - 테이블을 정의하는 명령문
   ```{.sql}
   CREATE TABLE 학생
       (이름 VARCHAR(15) NOT NULL,
       학번 CHAR(8),
       전공 CHAR(5),
       성별 SEX,
       생년월일 DATE,
       PRIMARY KEY(학번),
       FOREIGN KEY(전공) REFERENCES 학과(학과코드)
           ON DELETE SET NULL
           ON UPDATE CASCADE,
       CONSTRAINT 생년월일제약 CHECK(생년월일) = "1980-01-01));
   ```
5. CREATE VIEW
   - 뷰를 생성하는 명령문
   ```{.sql}
   CREATE VIEW sample
   AS SELECT
   FROM
   WHERE
   ```
6. CREATE INDEX
   - 인덱스를 정의하는 명령문
   ```{.sql}
   CREATE INDEX sample
   ON sample_table
   ```
7. ALTER TALBE
   - 테이블의 정의를 변경
   ```{.sql}
       ALTER TABLE 학생 ADD[ALTER, DROP COLUMN] 학년 VARCHAR(3)
   ```
8. DROP
   - DROP은 스키마, 도메인, 기본 테이브, 뷰 테이브, 인덱스, 제약 조건 등을 제거하는 명령문이다.
   - drop schema
   - drop domain
   - drop table
   - drop view
   - drop constraint

### DCL

1. DCL(DATA CONTROL LANGUAGE)의 개념
   - 데이터 제어어는 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는데 사용하는 언어이다.
2. GRANT/REVOKE
   - 권한을 부여하거나 최소하기 위한 명령어
   - GRANT sample TO 사용자
   - REVOKE sample FROM 사용자
3. COMMIT
4. ROLLBACK
5. SAVEPOINT

### DML

1. DML(Data Manipulation Languag)의 개념
   - DML은 데이터베이스 사용자가 응용 프로그램이나 질의어를 통해 저장된 데이터를 실질적으로 관리하는데 사용되는 언어이다.
2. INSERT INTO
3. DELETE FROM
4. UPDATE SET

### SELECT

### JOIN

    - Inner Join
    - Outer Join
    - Self Join
