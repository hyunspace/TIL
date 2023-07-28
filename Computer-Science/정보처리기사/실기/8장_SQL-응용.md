# SQL 응용

## DDL, DML, DCL

* DDL: CREATE, ALTER, DROP

  * **CREATE TABLE** 테이블명 ()

    ```SQL
    CREATE TABLE 직원(
    	사번 CHAR(15),
        이름 CHAR(4) NOT NULL,
        전화번호 CHAR(20),
        부서번호 CAHR(10),
        기본급 INT,
        PRIMARY KEY(사번),
        UNIQUE(전화번호),
        FOREIGN KEY(부서번호) REFERENCES 부서(부서번호),
        CHECK (기본급 >= 1000000)
    );
    ```

  * **CREATE VIEW** 뷰명 AS SELECT ~

    ```SQL
    CREATE VIEW 강좌교수(강좌명, 강의실, 수강인원제한, 교수이름)
    AS SELECT 강좌명, 강의실, 수강인원, 이름
    FROM 강좌, 교수
    WHERE 강좌.교수번호 = 교수.교수번호;
    ```

  * **ALTER TABLE** 테이블명 

    * ADD 속성명 데이터타입
    * ALTER 속성명
    * DROP COLUMN 속성명

* DCL: GRANT, REVOKE, ROLLBACK

  * GRANT 권한리스트 ON 개체 TO 사람 [WITH GRANT OPTION]
    * **WITH GRANT OPTION**: 받은 권한을 다시 다른 사람에게 부여할 수 있음
    
  * REVOKE [GRANT OPTION FOR] 권한리스트 ON 개체 FROM 사람
    * GRANT OPTION FOR: 다른 사용자에게 권한을 부여할 수 있는 권한을 취소
    
    ```sql
    -- SELECT 권한 + 다른 사람에게 부여 권한 모두 제거
    REVOKE SELECT ON 수강 FROM 박문수 CASCADE;
    -- SELECT 권한은 유지하되 다른 사람에게 부여할 수 있는 권한만 제거
    REVOKE GRANT OPTION FOR SELECT ON 수강 FROM 박문수;
    ```

* DML: SELECT, INSERT, DELETE, UPDATE

  * SELECT

    * **WHERE 절에서는 집계함수를 사용할 수 없다**

      ```SQL
      SELECT 상호, 총액
      FROM 거래내역
      WHERE 총액 IN (SELECT MAX(총액) FROM 거래내역);
      ```

  * INSERT INTO 테이블명 ([속성명1, ...]) VALUES (데이터1, ...)
  * DELETE FROM 테이블명 [WHERE 조건]
  * UPDATE 테이블명 SET 속성명=데이터 [WHERE 조건]




## 연산자와 조인

### 집합 연산자

* UNITON
* UNION ALL
* INTERSECT
* EXCEPT



### JOIN

* INNER JOIN

  ```SQL
  FROM 테이블명1, 테이블명2
  WHERE 테이블명1.속성명 = 테이블명2.속성명
  ```

* OUTER JOIN

  ```SQL
  FROM 테이블명1 LEFT[RIGHT] OUTER JOIN 테이블명2
  ON 테이블명1.속성명 = 테이블명2.속성명
  ```



## 관련 기술

### DBMS 접속 기술

* ODBC
  * 마이크로소프트에서 출시한 표준 개방형 API
* MyBatis
  * JDBC 코드를 단순화하여 사용할 수 있는 SQL Mapping 기반 오프 접속 프레임워크
* ORM(Object-Relational Mapping)
  * 객체지향 프로그래밍의 객체와 관계형 데이터베이스의 데이터를 연결하는 기술
