### SELECT

- SELECT 문은 테이블에서 원하는 정보를 불러올 때 사용하는 문법
- 테이블의 열에 속하는 데이터를 불러온다.
- \*은 모든 것을 가져오는 것을 뜻함

```{.sql}
SELECT col1, col2, ....
FROM table_name;
```

### DISTINCT

- 중복을 배제하고 고유값만을 출력하고자 할 때 사용 ( SELECT와 같이 사용 )

```{.sql}
SELECT DISTINCT col1, col2, ...
FROM table_name;
```

### WHERE

- 조건을 걸어 검색하고자 할 때 사용

```{.sql}
SELECT col1, col2, ...
FROM table
WHERE condition;
```

- 비교 연산자
  - 같을 때 "="
  - 같지 않을 때 "!=", "<>"
  - 클 때 "<"
  - 크거나 같을 때 "<="

### AND, OR, NOT

- 복합 연산자

```{.sql}
SELECT col1, col2, ...
FROM table
WHERE condition1 and condition2;

SELECT col1, col2, ....
FROM table
WHERE condition1 or condition2;

SELECT col1, col2, ...
FROM table
WHERE NOT condition;
```

### ORDER BY

- 결과를 오름차순이나 내림차순으로 정렬

```{.sql}
SELECT col1, col2, ...
FROM table
ORDER BY col1 ASC|DESC;

SELECT col1, col2, ...
FROM table
ORDER BY FIELD (col1, order1, order2, ...);
```

### LIMIT

- 출력 결과의 갯수를 제한

```{.sql}
SELECT * FROM table LIMIT 3;
SELECT * FROM table LIMIT 2, 3;
SELECT * FROM table LIMIT 0, 4;
```

### NULL VALUE

- 값이 NULL인 값을 검색

```{.sql}
SELECT col1, col2, ...
FROM table
WHERE col_name IS NOT NULL;

SELECT col1, col2, ...
FROM table
WHERE col_name IS NULL;
```

### LIKE

- 특정 패턴을 탐색

```{.sql}
SELECT col1, col2, ...
FROM table
WHERE col_name LIKE pattern;
```

- %, \_
  - % : 0개 문자 혹은 여러 개의 문자를 의미
  - \_ : 하나의 문자를 의미

### IN()

- WHERE 절 내 여러 값을 설정하고 할 때 사용

```{.sql}
SELECT col
FROM table
WHERE col_name IN (val1, val2, ...);
```

### BETWEEN

- WHERE 절 내 검색 조건으로 범위를 지정하고자 할 때 사용

```{.sql}
SELECT col1
FROM table
WHERE col_name BETWEEN val1 AND val2;
```

### JOIN

- 두 개나 그 이상의 테이블의 행을 서로 결합하고자 할 때
- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN 이 존재

```{.sql}
SELECT col1
FROM table1 INNER JOIN table2
ON table1.col = table2.col;

SELECT col1
FROM table1 LEFT INNER JOIN table2
ON table1.col = table2.col;

SELECT col1
FROM table1 RIGHT JOIN table2
ON table1.col = table2.col;

SELECT col1
FROM table1 FULL OUTER JOIN table2
ON table1.col = table2.col;
```

### UNION

- SELECT의 컬럼 리스트를 기준으로 두 개 이상의 질의 결과를 하나의 테이블로 합치고자 할 때

```{.sql}
SELECT col FROM table1
UNION
SELECT col FROM table2;
```

- 주의 사항
  - UNION은 기본저긍로 중복값을 제거함, 제거하고 싶지 않을 때는 UNION ALL을 사용해야 한다.

### MIN, MAX, ABS, COUNT, AVG, SUM

```{.sql}
SELECT MIN (col) FROM table;
SELECT MAX (col) FROM table;
SELECT ABS (col) FROM table;
SELECT COUNT (col) FROM table;
SELECT AVG (col) FROM table;
SELECT SUM (col) FROM table;
```

### GROUP BY

- 집계함수와 함께 사용되어, 결과를 지정한 칼럼에 따라 그룹으로 묶고자 할 때

```{.sql}
SELECT col1
FROM table
WHERE condition
GROUP BY col_name;
```

### HAVING

- WHERE 조건을 걸 수 없는 집계함수에 조건을 걸고자 할 때 사용

```{.sql}
SELECT col1
FROM table
WHERE condition
GROUP BY col_name
HAVING condition;
```

### CONCAT

- 여러 문자열을 하나로 합치고자 할 때 사용

```{.sql}
SELECT CONCAT(str1, str2, str3, ...);
```

### ROUND(), TRUNC()

- ROUND는 반올림, TRUNC는 버림

```{.sql}
SELECT ROUND|TRUNC (val, digit)
FROM table
```
