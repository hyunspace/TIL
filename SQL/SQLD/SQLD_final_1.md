# SQLD 막판 최종 정리

## SQL 명령문 개괄

1. FROM - WHERE - GROUP BY - HAVING -SELECT - ORDER BY

2. DML, DDL, TCL
   * DML: SELECT, INSERT, DELETE, UPDATE
   * DDL: ALTER, CREATE, MODIFY, DROP
   * TCL: ROLLBACK, COMMIT
   * DCL: GRANT, REVOKE



## SELECT

* DISTINCT(집약): 중복된 정보를 집약

  * DISTINCT deptno, mgr

    = GROUP BY deptno, mgr

### AS

* SELECT 뒤에서
  * 생략 가능
  * 컬럼명에 띄어쓰기가 있다면 `""`
* FROM 다음에는 절대 사용 불가

### CONCAT

> 인수가 무조건 두 개

* `+` : SQL server
* `||` : Oracle



## 논리연산자

* ` AND`
* `OR`
* `NOT`

> `연산자의 연산 순위`
>
> 1. NOT
>
> 2. AND
>
> 3. OR
>
> ( (NOT 조건) AND 조건 AND (NOT 조건) ) OR 조건



## SQL 연산자

* A BETWEN 1 AND 2

  1 <= A <= 2

* A IN (1, 2, 3)

  A = 1 OR A = 2 OR A = 3

#### LIKE

* `_` : 미지의 한 글자
* `%` : 0 이상의 글자
* `ESCAPE` : 와일드카드 (`_`, `%`)를 문자로 취급
  * LIKE 'A`@`_A' ESCAPE `@`
  * @자리에는 아무 문자나 쓸 수 있음 => 내가 원하는 문자로 설정하는 것

#### ROWNUM (ORACLE)

* WHERE 절에서 ROWNUM 이 1인 경우 무조건 포함

* 실행 순서

  ```sql
  SELECT empno, sal FROM emp
  WHERE rownum <= 3
  ORDER BY sal
  ```

  * **정렬 전**, 기존 데이터에서 3개를 뽑고 난 뒤에 정렬

#### TOP (SQL Server) 

* SELECT 절 옆에 사용
* `TOP n 컬럼명` : 특정 컬럼명을 출력할 때, 상위 n개 행을 가져온다



## NULL

1. NULL의 정의

   * 부재, 모르는 값

2. NULL 의 연산

   * 산술 연산

     * NULL + 2, NULL - 4, NULL * NULL => NULL

   * 비교 연산

     * NULL = NULL, NULL = 2

       => 알 수 없음 (unknown)

     * WHERE절 뒤의 조건이 unknown이라면, **FALSE** 처리

3. 정렬 상 의미

   * Oracle: 무한대. 맨 마지막에 나옴(ASC)
   * SQL Server: - 무한대. 맨 처음에 나옴(ASC)

4. 관련 함수

   * **NVL**(값1, 값2), **NVL2**(값1, 값2, 값3), **ISNULL**(값1, 값2) : 널뛰기
     * `값1` 이 NULL이면 `값2`
     * `값1` 이 NULL이면 `값3`, 아니면 `값2`
   * **NULLIF**(값1, 값2) : 같이 놀자
     * 두 개의 값이 같으면 NULL
     * 다르면 값1
   * **COALESCE**(값1, 값2, ... ) : NULL이 아닌 첫 번째 값
     * 값1,값2, 값3, ... 중에서 처음으로 NULL이 아닌 값 반환



## 정렬

* 정렬의 특성
  1. 가장 마지막에 실행
  2. 성능이 느려질 수 있음
  3. NULL 값과의 관계

* 컬럼 번호 정렬
  * 출력 되는 컬럼의 수보다 큰 값 불허
* 인수 두 개 정렬
  * 앞에 인수 값이 같으면 뒤의 것으로 판단
* SELECT 뒤에 쓰지 않은 컬럼으로도 정렬 가능



## 숫자 함수

#### ROUND

* 자리수 확인하기

#### CEIL / CEILING

> 오라클 / SQL Server



## 문자열 함수

#### UPPER, LOWER

#### Lpad, Rpad, Ltrim, Rtrim

#### SUBSTR, NSTR

* 실습 꼭 해보기



## 날짜 함수

#### TO_CHAR, TO_DATE

* 형변환 되는가? `YES`

#### SYSDATE / GETDATE()

> 오라클 / SQL Server

#### 날짜데이터 + 100

* 숫자를 더하면, 기본 값은 day로 인식



## DECODE/CASE

* CASE WHEN <> THEN <> ...
  * ELSE가 없다면, 조건 만족하지 않을 때 NULL이 나온다



## 집계 함수

* null과의 관계 (35회 기출 문제)

  |  A   |  B   |  C   | A+B+C |
  | :--: | :--: | :--: | :---: |
  | null | null |  1   | null  |
  |  3   |  2   |  2   |   7   |
  | null |  2   |  3   | null  |

  * SUM(A) = 3, COUNT(A) = 1
  * SUM(B) = 4, COUNT(B) = 2 ** 확인해보기
  * SUM(A+B+C) = 7



## GROUP BY

* 집약 기능
* 그룹 수준으로 정보를 바꾼다



## JOIN

1. **NATURAL JOIN, USING**

   * 중복된 컬럼이 하나만 출력
   * 중복된 컬럼이 제일 앞에 등장

2. **LEFT OUTER JOIN**

   * `A LEFT OUTER JOIN B`

     39분 다시 듣기

3. 조인순서; FROM A, B, C

   1. A, B 먼저 조인하고 결과 테이블과 C를 조인



## 서브쿼리

|          |                   서브쿼리                    |
| :------: | :-------------------------------------------: |
|  SELECT  |                    SCALAR                     |
|   FROM   | INLINE VIEW<br /> 메인 쿼리의 컬럼 사용 가능! |
|  WHERE   |     거의 모든 서브 쿼리 => 중첩 서브쿼리      |
| GROUP BY |                       X                       |
|  HAVING  |     거의 모든 서브 쿼리 => 중첩 서브쿼리      |
| ORDER BY |                    SCALAR                     |

* 40분 대 설명 다시 들어보기
* IN, ANY/SOME, ALL, EXIST



## 집합 연산자

|  집합 연산자   |           의미            |                  정렬 작업                   |
| :------------: | :-----------------------: | :------------------------------------------: |
|     UNION      |          합집합           |                      O                       |
|   INTERSECT    |          교집합           |                      O                       |
| MINUS (EXCEPT) |          차집합           |                      O                       |
|   UNION ALL    | 단순 더하기<br />(중복 O) | X<br />빠르다<br />but 중복데이터 존재<br /> |

* UNION vs UNION ALL
  * 후자가 빠르다



##  DDL

* TRUNCATE vs. DROP
  * 전자는 데이터만 사라지고, 구조가 남음
  * 후자는 모두 삭제!
* TRUNCATE vs. DELETE
  * DDL vs. DML
  * rollback, commit과 함께 문제가 나옴



## DML

#### INSERT

* 컬럼의 수와 values의 수가 다르면 오류 발생

#### UPDATE

#### DELETE



#### MERGE

> 기출문제 37회 보기





## 제약 조건 ⭐️⭐️✔

> pk, unique, not null

#### Primary Key

* 대표성을 가지므로 하나만 존재
* UNIQUE + NOT NULL



## DCL

#### GRANT

#### REVOKE

* 37회 기출 문제 ON TO 보기



#### role 특징 5개

* 명령어가 아님. 객체(object).



## VIEW

* 독립성
* 편리성
* 보편성





## 그룹 함수 ⭐️⭐️⭐️

> 결과값을 주고 어떤 함수를 사용한 건지 질문
>
> 1.  null 다 찾고
> 2. 총합행이 있는가 => 있다면 roll up 또는 cube
>    1. 있다면 roll up 또는 cube
>       * 둘 다 결과가 있다면(행의 수가 많아 보이면) cube
>       * 계층화 되어 있다면(행의 수가 적어 보이면) roll up
>    2. 없다면 grouping sets

#### ROLL UP

* ROLL UP (A, B) != ROLL UP (B, A)
  * 같은 결과 X

#### CUBE

* CUBE (A, B) = CUBE (B, A)

#### GROUPINGSETS

#### GROUPING



## TCL

#### commit

* auto commit off & begin transaction
  * DDL에 커밋 기능 없애기

#### rollback

