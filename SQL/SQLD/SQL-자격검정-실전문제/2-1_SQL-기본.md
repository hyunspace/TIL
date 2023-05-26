# 2-1. SQL 기본

1. 관계형 데이터베이스 개요
2. DDL
3. DML
4. TCL
5. WHERE절
6. 함수
7. GROUP BY, HAVING절
8. ORDER BY절
9. 조인(JOIN)

<br/>

## 관계형 데이터베이스 개요

### SQL 명령문 개괄

* DML `데이터 조작`
  * SELECT, INSERT, DELETE, UPDATE
* DDL `데이터 정의: 만들고 바꾸고 수정하고 삭제하고`
  * CREATE, ALTER, MODIFY, DROP
* TCL `트랜잭션 제어: 확정지었다, 되돌렸다`
  * COMMIT, ROLLBACK
* DCL `데이터 제어: 권한을 줬다 뺏었다`
  * GRANT, REVOKE

<br/>

## DDL

> CREATE, ALTER, MODIFY, DROP

### CREATE

* 제약 조건
  * UNIQUE: 중복X, null 허용
  * PK: UNIQUE + NOT NULL
* FK관계 참조 동작
  * DELETE: 마스터 삭제시 child는?
    * cascade: 같이 삭제
    * restrict: child 테이블에 PK없을 때만 마스터 삭제 가능
    * no action: 참조무결성 위반하는 삭제/수정 X
  * INSERT: child에 새로운 값 입력할 때
    * automatic 자동으로 마스터 PK 생성 후 입력
    * dependent 마스터 테이블에 PK있을 때만 입력 가능
    * no action

### ALTER

* SQLServer에서는 여러 개의 컬럼 동시 수정 불가능하다

* 스키마 변경할 때(컬럼명 바꾸고 싶을 때)

  ```sql
  ALTER TABLE 테이블명
  DROP COLUMN 컬럼명
  ```

<br/>

## DML

> SELECT, INSERT, DELETE, UPDATE

### SELECT

* DISTINCT(집약): 중복된 정보를 집약

  * DISTINCT deptno, mgr

    = GROUP BY deptno, mgr

* AS

  * SELECT 뒤에서
    * 생략 가능
    * 컬럼명에 띄어쓰기가 있다면 `""`
  * FROM 절에서는 절대 사용 불가

* CONCAT
  * 인수가 무조건 두개
  * `+` : SQLServer
  * `||` : Oracle

* TOP (SQL Server) 

  * SELECT 절 옆에 사용

  * `TOP n 컬럼명` : 특정 컬럼명을 출력할 때, 상위 n개 행을 가져온다

* 공백문자 `''`의 경우, 오라클은 null로 인식, SQLServer는 공백문자로 인식

#### TRUNCATE vs. DROP vs. DELETE ⭐️

|                           TRUNCATE                           |                             DROP                             |                  DELETE                   |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------: |
|                   DDL<br />(DML성격 있음)                    |                             DDL                              |                    DML                    |
|                       rollback 불가능                        |                       rollback 불가능                        |               rollback 가능               |
|                         auto commit                          |                         auto commit                          |               사용자 commit               |
|  최초 테이블의 용량만<br />데이터의 디스크 사용량은 초기화   |           용량 비워짐<br />디스크 사용량 초기화 O            | 용량은 그대로<br />디스크 사용량 초기화 X |
| 테이블 구조만 남기고 데이터 삭제<br />테이블 생성 초기 상태로 (인덱스도 삭제) | 테이블 구조 포함 모두(공간, 객체) 삭제 <br />테이블 정의 자체가 삭제 |               데이터만 삭제               |

* DELETE는 로그가 남고, 원복 가능하다는 것!

<br/>

## TCL⭐️

#### commit

* auto commit off & begin transaction
  * DDL에 커밋 기능 없애기

#### rollback



### 트랜잭션 transaction

* 특징
  * 원자성: all or nothing
  * 일관성: 잘못 없는 상태에서 실행했으면, 그 결과도 잘못 없는 상태여야 함
  * 고립성: 실행 중에 다른 트랜잭션의 영향 X
  * 지속성: 트랜잭션 성공 시 영구 저장
* 격리성이 낮으면
  * dirty read: 다른 트랜잭션에 의해 수정+커밋 된 것 모르고 그 전의 것 읽는 문제
  * non-repeatable read: 같은 키를 가진 행을 두 번 읽었는데 그 사이에 변경/삭제되어 다른 결과가 나오는 문제
  * phantom read: 같은 쿼리를 두번 실행 했는데 전에 없던 유령 레코드가 나옴

<br/>

## WHERE

#### ROWNUM (ORACLE) ⭐️

* WHERE 절에서 ROWNUM 이 1인 경우 무조건 포함

* 실행 순서

  ```sql
  SELECT empno, sal FROM emp
  WHERE rownum <= 3
  ORDER BY sal
  ```

  * **정렬 전**, 기존 데이터에서 3개를 뽑고 난 뒤에 정렬

<br/>

## 함수

> 함수 = 사용자정의 + 내장함수
>
> 내장함수는 입력행 수에 따라서 단일행 함수 or 다중행 함수
>
> 다중행 함수 = 집계+그룹_윈도우 함수

* 내장함수는 모두 단일값을 반환한다

### 단일행 함수

* SELECT, WHERE, ORDER BY, UPDATE의 SET 절에 사용 가능

#### 숫자 함수⭐️

* ROUND
* CEIL / CEILING

#### 문자열 함수⭐️

* UPPER, LOWER
* LPAD, RPAD, LTRIM, RTRIM
* SUBSTR, NSTR

#### 날짜 함수⭐️

* TO_CHAR, TO_DATE
  * 형변환 되는가? `YES`


* SYSDATE / GETDATE()

  > 오라클 / SQL Server

* 날짜데이터 + 100
  * 숫자를 더하면, 기본 값은 day로 인식

### CASE

* ELSE 가 없으면, 조건 다~ 만족 못하면 null값 나옴

```sql
-- 두 개 같음
CASE WHEN code = 10 THEN 100
ELSE

CASE code WHEN 10 THEN 100
ELSE
```

### DECODE

* DECODE(확인할 컬럼/식, 조건1, 결과1, 조건2, 결과2, ...)

### NULL 관련 ⭐️

* NULL의 정의
  * 부재, 모르는 값

- NULL 의 연산

  * 산술 연산

    * NULL + 2, NULL - 4, NULL * NULL => NULL

  * 비교 연산

    * NULL = NULL, NULL = 2

      => 알 수 없음 (unknown)

    * WHERE절 뒤의 조건이 unknown이라면, **FALSE** 처리

  * **SUM이나 AVG함수를 사용하면 null값 무시하고 계산 됨**

- 정렬 상 의미

  * Oracle: 무한대. 맨 마지막에 나옴(ASC)
  * SQL Server: - 무한대. 맨 처음에 나옴(ASC)

- 관련 함수⭐️⭐️

  * **NVL**(값1, 값2), **ISNULL**(값1, 값2)
    * `값1` 이 NULL이면 `값2`
  * **NVL2**(값1, 값2, 값3)  *널 뛰기*
    * `값1` 이 NULL이면 `값3`, 아니면 `값2`
  * **NULLIF**(값1, 값2)  *같이 놀자*
    * 값1과 값2가 같으면 NULL
    * 다르면 값1
  * **COALESCE**(값1, 값2, ... ) : NULL이 아닌 첫 번째 값
    * 값1,값2, 값3, ... 중에서 처음으로 NULL이 아닌 값 반환

- 집계 함수⭐️

  - count(*): null 포함 행의 수
  - count(exp): null 제외
  - sum: null 제외 합계
  - avg: null 행 제외 평균
  
  |  A   |  B   |  C   | A+B+C |
  | :--: | :--: | :--: | :---: |
  | null | null |  1   | null  |
  |  3   |  2   |  2   |   7   |
  | null |  2   |  3   | null  |

## GROUP BY, HAVING

#### `FROM - CONNECT BY - WHERE - GROUP BY - HAVING - SELECT - ORDER BY`

### GROUP BY

* 집계 기준이 아닌 컬럼은 SELECT 불가능
* 집계 count로 ORDER BY 가능
* 집계 관련 조건 추가하고 싶을 땐 HAVING!
  * WHERE 절 처리할 때는 GROUP BY 가 등장하기 전이므로

## ORDER BY

* 정렬의 특성
  1. 가장 마지막에 실행
  2. 성능이 느려질 수 있음
  3. NULL 값과의 관계

* 컬럼 번호 정렬
  * 출력 되는 컬럼의 수보다 큰 값 불허
* 인수 두 개 정렬
  * 앞에 인수 값이 같으면 뒤의 것으로 판단
* SELECT 뒤에 쓰지 않은 컬럼으로도 정렬 가능

<br/>

## JOIN

* 일반적으로 join은 PK와 FK 값의 연관성에 의해 성립된다
* DBMS 옵티마이져는 FROM 절에 나열된 테이블들이 아무리 많아도 항상 2개씩 짝을 지어서 join을 수행한다
* EQUI Join은 Join에 관여하는 테이블 간의 컬럼 값들이 정확하게 일치하는 경우에 사용되는 방법이다
* EQUI Join은 '=' 연산자에 의해서만 수행되며, 그 이외의 비교 연산자를 사용하는 경우에는 모두 Non EQUI Join이다
* 대부분 Non EQUI Join을 수행할 수 있지만, 때로는 설계상의 이유를 수행이 불가능한 경우도 있다

