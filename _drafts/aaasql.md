---
excerpt: "PostgreSQL 위주로 세팅 방법 및 Query문 정리"
title: "SQL"
header:
  teaser: "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/SQL-Products-Option-Light_v1_RE4xfAg?resMode=sharp2&op_usm=1.5,0.65,15,0&wid=610&qlt=100&fmt=png-alpha&fit=constrain"
categories:
  - Cheatsheet
tags:
  - SQL
last_modified_at: YYYY-MM-DDT00:30:30+09:00
---

<div class="notice--info" markdown="1">
⚙️ **Docker 기반 PostgreSQL + DBeaver 설정 방법 (macOS)**

---

**Docker Desktop 설치**
- PostgreSQL 컨테이너 실행 환경
- 컨테이너 상태 / 로그 확인용 GUI

**DBeaver 설치**
- DB 접속
- 스키마·테이블 시각화
- SQL 쿼리 실행

---

**Docker Desktop 실행**
- 메뉴바의 🐳 아이콘이 Running 상태인지 확인
- Docker 엔진이 실행된 상태에서만 PostgreSQL 컨테이너를 생성·실행할 수 있음

---

**프로젝트 디렉토리 구성**

```text
project-root/
├─ docker-compose.yml     <- PostgreSQL 서버 설정
└─ init/                  <- DB 초기화 SQL (번호를 붙여서 관리 가능)
    ├─ 01_schema.sql
    ├─ 02_data.sql
```

---

**docker-compose.yml 작성** (서버 설정)

```yml
services:
    postgres:
    image: postgres:17                # PostgreSQL 17이 설치된 리눅스 환경 실행
    container_name: postgres-db
    restart: always                   # Docker Desktop 재실행 시 컨테이너 자동 실행

    environment:
        POSTGRES_USER: postgres         # DBeaver setting → Username
        POSTGRES_PASSWORD: password     # DBeaver setting → Password
        POSTGRES_DB: user               # DBeaver setting → Database

    ports:
        - "5432:5432"                   # DBeaver setting → Port

    volumes:
        # 컨테이너 종료 후에도 DB 데이터 유지
        - postgres_data:/var/lib/postgresql/data
        # DB 데이터 볼륨이 최초 생성될 때 1회만 실행됨
        - ./init/01_schema.sql:/docker-entrypoint-initdb.d/01_schema.sql
        - ./init/02_data.sql:/docker-entrypoint-initdb.d/02_data.sql

volumes:
    postgres_data:
```

---

**프로젝트 디렉토리에서 컨테이너 실행**

*DB 컨테이너 실행*
```bash
docker compose up -d
```
`-d`: 백그라운드 실행(권장)

*DB 컨테이너 중지 및 삭제*
```bash
docker compose down
```
컨테이너는 일회용이지만 데이터를 저장한 볼륨은 남아있기 때문에 다시 up해서 불러올 수 있음

*DB 완전 초기화*
```bash
docker compose down -v
```
`-v`: 볼륨까지 영구 삭제 (스키마나 초기 데이터셋을 변경할 경우 초기화 필요)

---

**DBeaver로 DB 접속**
- 첫 실행 시 `New Database Connection`으로 연결
   - Driver: `PostgreSQL`
   - Connection Settings:
      - Connect by: `Host`
      - Host: `localhost`
      - Database, Port, Username, Password → `docker-compose.yml`의 값과 동일
- 연결 시 팝업이 뜨면 'Download'를 클릭하여 자동으로 드라이버를 설치
</div>

<br>

## Database Structure

### CREATE Database

```sql
CREATE DATABASE university_db;
```

### CREATE Schema

```sql
CREATE SCHEMA academic;
```
- 스키마는 DB 안의 네임스페이스(폴더) 개념
- 테이블 이름 충돌 방지, 도메인/팀 단위 분리 목적
- 스키마를 지정하지 않으면 기본값인 `public`에 테이블이 생성됨

### search_path

```sql
SHOW search_path;
```
- 테이블명만 사용했을 때 참조할 스키마 순서 확인
- 기본값: `"$user"`, `public`

```sql
SET search_path TO academic, public;
```
- 스키마 검색 우선순위 변경 (1순위 academic, 2순위 public)
- academic 스키마 내의 테이블은 `academic.` 접두사 없이 호출 가능

<br>

## Execution Order

1. `FROM`      : 어떤 테이블에서 데이터를 가져올지 결정 (+ `JOIN` 함께 실행)
2. `WHERE`     : 개별 행을 조건에 맞게 먼저 필터링
3. `GROUP BY`  : 남은 행들을 특정 컬럼 기준으로 그룹화 (집계 함수는 그룹화 후 사용)
4. `HAVING`    : 그룹화된 결과물 중에서 조건에 맞는 그룹만 다시 필터링
5. `SELECT`    : 출력할 컬럼 선택 및 별칭 부여
6. `DISTINCT`  : 중복된 행을 하나로 병합
7. `ORDER BY`  : 모든 결과가 나온 뒤 마지막으로 정렬 (별칭 사용 가능)
8. `LIMIT`     : 정렬된 결과의 최상단부터 필요한 만큼만 잘라서 출력

<br>

## Data Definition

### CREATE table

```sql
CREATE TABLE academic.학과 (
    학과번호 INT PRIMARY KEY,       -- 컬럼명 컬럼타입 나열
    학과명 TEXT NOT NULL,
    학과사무실 TEXT,
    교수명 TEXT
);

CREATE TABLE academic.수강생 (
    수강생번호 SERIAL PRIMARY KEY,   -- PRIMARY KEY
    성명 TEXT,
    학과명 TEXT,
    평점 FLOAT,
    이수학점 INT,
    자격증보유 BOOLEAN DEFAULT FALSE,
    생년월일 TEXT,
    주소 TEXT,
    이메일 TEXT UNIQUE,
    FOREIGN KEY (학과번호)          -- FOREIGN KEY
        REFERENCES 학과(학과번호)    
        ON DELETE CASCADE
);

CREATE TABLE academic.교수 (
    교수번호 INT,
    교수_성 TEXT,
    교수_이름 TEXT
);
```
- `SERIAL`은 내부적으로 **INT + SEQUENCE** 성질을 지니고 있어 자동으로 숫자가 증가
- `UNIQUE`는 중복 데이터를 비허용하는 옵션
- `NOT NULL`은 칸이 비어있는 NULL 상태를 비허용하는 옵션
- `DEFAULT`는 아무 값도 넣지 않았을 때 NULL 대신 설정한 기본값으로 채움
- `PRIMARY KEY` : 행을 유일하게 식별하는 키로, 중복 불가 + NULL 불가
- `FOREIGN KEY` : 수강생 테이블의 **학과번호** 컬럼은 반드시 다른 테이블(학과)에 존재해야 외래키로 사용 가능
   - `ON UPDATE` + `조건` : 부모 테이블의 데이터가 수정될 때 자식 테이블의 데이터 처리 방법
   - `ON DELETE` + `조건` : 부모 테이블의 데이터가 삭제될 때 자식 테이블의 데이터 처리 방법

<div class="notice--success" markdown="1">
✏️ 참조 무결성 제약 조건 5가지

**CASCADE**     
부모 테이블의 데이터가 수정/삭제되면 이를 참조하는 자식 테이블의 데이터도 함께 수정/삭제

**SET NULL**      
부모 테이블의 데이터가 수정/삭제되면 자식 테이블의 해당 외래키 값을 NULL로 변경   
(단, 외래키 컬럼이 NOT NULL이 아니어야 가능)

**SET DEFAULT**      
부모 테이블의 데이터가 수정/삭제되면 자식 테이블의 외래키 값을 미리 설정해둔 기본값으로 변경

**RESTRICT**     
자식 테이블에서 해당 데이터를 참조하고 있다면 부모 테이블의 데이터를 수정/삭제할 수 없도록 차단     
(변경 시도 시 에러 발생)

**NO ACTION**     
RESTRICT과 유사하나 SQL 제약 조건 체크를 트랜잭션 끝으로 미룰 수 있음     
(대부분의 DB에서 기본값으로 사용됨)
</div>

### ALTER table

#### ADD column

```sql
ALTER TABLE 수강생
ADD COLUMN 성별 INT;           -- 남자는 1, 여자는 2로 저장되는 컬럼 추가
```

#### DROP column

```sql
ALTER TABLE 수강생
DROP COLUMN 학과명;
```

#### ADD/DROP constraint

```sql
-- ADD PRIMARY KEY 조건
ALTER TABLE 교수
ADD CONSTRAINT pk_교수_교수번호 PRIMARY KEY (교수번호);

-- ADD FOREIGN KEY 조건
ALTER TABLE 학생
ADD CONSTRAINT fk_학생_학과번호
FOREIGN KEY (학과번호)
    REFERENCES 학과(학과번호)
    ON DELETE SET NULL;     -- 새 조건

-- ADD UNIQUE 조건
ALTER TABLE 학생
ADD CONSTRAINT uk_학생_이메일 UNIQUE (이메일);
```
- `DROP`도 가능

#### SET/DROP column value

```sql
ALTER TABLE 수강생
ALTER COLUMN 이수학점 SET DEFAULT 0;    -- DEFAULT 값 설정

ALTER TABLE 수강생
ALTER COLUMN 이수학점 DROP DEFAULT;     -- DEFAULT 값 삭제

ALTER TABLE 수강생
ALTER COLUMN 성명 SET NOT NULL         -- NOT NULL 조건 설정

ALTER TABLE 수강생
ALTER COLUMN 성명 DROP NOT NULL;       -- NOT NULL 조건 삭제 
```

#### change column type

| 기능           | 표준 SQL / PostgreSQL 문법                                           | MySQL 전용 문법                       |
|--------------|---------------------------------------------------------------------|--------------------------------------|
| 타입 변경      | `ALTER` COLUMN 성별 `TYPE` TEXT                                      | `MODIFY` COLUMN 성별 VARCHAR(10)      |
| 이름+타입 변경 | `RENAME` COLUMN 성별 `TO` gender<br>`ALTER` COLUMN gender `TYPE` TEXT | `CHANGE` COLUMN 성별 gender VARCHAR(10) |

```sql
-- PostgreSQL 전용 문법 (:: 연산자 사용)
ALTER TABLE 수강생
ALTER COLUMN 성별 TYPE TEXT     -- 기존 INT 타입 데이터를 TEXT 타입으로 변경
USING 성별::TEXT;               -- USING으로 명시적 형변환

-- 표준 SQL 문법 (CAST 함수 사용)
ALTER TABLE 수강생
ALTER COLUMN 성별 TYPE TEXT
USING CAST(성별 AS TEXT);
```
- 형변환 명시 없이도 자동으로 변환되는 경우
   - INT → BIGINT (작은 정수에서 큰 정수)
   - INT → NUMERIC/FLOAT (정수에서 실수)
   - CHAR → VARCHAR/TEXT (고정 길이에서 가변 길이)
   - DATE → TIMESTAMP
   - TIMESTAMP → TIMESTAMPTZ
   - BOOLEAN/INT → TEXT
- 명시적 형변환이 필수인 경우
   - TEXT → INT, NUMERIC, DATE (문자열 안의 글자 처리)
   - FLOAT → INT (소수점 아래 처리)
- PostgreSQL 사용 시 DEFAULT 값이 설정됐을 경우 먼저 `DROP DEFAULT`로 해제하는 것이 안전

```sql
ALTER TABLE 수강생
ALTER COLUMN 성별 TYPE TEXT
USING CASE 성별                -- 데이터 재배치 (1 -> '남', 2 -> '여')
        WHEN 1 THEN '남'
        WHEN 2 THEN '여'
        ELSE '미지정'
      END;
```
- `CASE WHEN` 패턴 사용

#### change table name

```sql
ALTER TABLE 수강생
RENAME TO 학생;
```

#### change column name

```sql
ALTER TABLE 학생
RENAME COLUMN 수강생번호 TO 학생번호;
```

<br>

## Data Manupulation

### INSERT (create)

```sql
INSERT INTO 학과(학과번호, 학과명, 학과사무실, 교수명)
VALUES (101, '컴퓨터공학과', '공학관 301호', '김철수');  -- 1개 행 삽입

INSERT INTO 학과(학과번호, 학과명, 학과사무실, 교수명)
VALUES
  (102, '전자공학과', '공학관 402호', '이영희'),
  (103, '심리학과', '인문관 101호', '박민준'),
  (104, '경영학과', '경상관 205호', '최지우');          -- 여러 행 삽입
```
- 컬럼과 값의 수는 반드시 동일하게 작성
- 생략된 컬럼은 반드시 `DEFAULT` 값을 가지거나 `NULL` 값을 허용하도록 설정 필요

```sql
INSERT INTO 학과 (학과번호, 학과명, 학과사무실, 교수명)
VALUES (
  105, 
  '데이터과학과', 
  (SELECT 학과사무실 FROM 학과 WHERE 학과번호 = 101), -- 학과번호가 101인 학과와 같은 사무실 사용
  '정우성'
);
```
- 값을 하드코딩하는 대신 다른 행의 특정 값을 복사해올 수 있음
- 괄호 안 서브쿼리는 반드시 단 하나의 값(1행1열)만 반환해야 함

### SELECT (read)

```sql
SELECT * FROM 스키마명.학생;    -- 테이블의 모든 컬럼 출력

SELECT 학생번호, 성명, ...      -- 테이블에서 특정 컬럼만 선택하여 출력
FROM 학생;
```

#### DISTINCT 

```sql
SELECT DISTINCT(학과번호)   -- 학생들이 속한 학과 종류를 확인 가능
FROM 학생;
```
- 중복 제거

#### LIMIT 

```sql
SELECT 학생번호, 평점
FROM 학생
ORDER BY 평점 DESC
LIMIT 10;           -- 평점 높은 순으로 10명만 출력
```
- 출력되는 행의 최대 개수를 제한

#### ORDER BY
```sql
SELECT 학생번호, 성명, 성별
FROM 학생
ORDER BY 학생번호 DESC;
```
- 결과값 정렬
- `ASC` : 오름차순(기본값, 생략 가능)
- `DESC` : 내림차순

#### WHERE 

```sql
SELECT 학생번호, 평점
FROM 학생
WHERE 평점 > 4.1;

SELECT 학생번호, 평점, 자격증보유
FROM 학생
WHERE 평점 > 4.1 AND 자격증보유 = TRUE;     -- true일 경우 생략 가능
```
- 특정 조건에 맞는 행만 추출
- 비교 연산자: `>`, `>=`, `<`, `<=`, `=`, `<>` 또는 `!=` (같지 않음)
- 논리 연산자: `AND` (전부 만족), `OR` (하나라도 만족), `NOT` (부정)

#### BETWEEN 

```sql
SELECT 학생번호, 평점
FROM 학생
WHERE 평점 BETWEEN 4.0 AND 4.5;      -- 4.0 이상 4.5 이하(시작과 끝 포함)

SELECT 학생번호, 평점
FROM 학생
WHERE 평점 >= 4.0 AND 평점 <= 4.5;    -- 위와 동일
```
- 지정한 범위 내의 값을 필터링

#### IN

```sql
SELECT 학생번호, 학과번호
FROM 학생
WHERE 학과번호 IN (3493, 4054, 4237);

SELECT 학생번호, 학과번호
FROM 학생
WHERE 학과번호 = 3493 OR 학과번호 = 4054 OR 학과번호 = 4237;  -- 위와 동일
```
- 목록에 포함된 값들 중 하나라도 일치하는지 확인

#### LIKE (vs ILIKE)

|               **LIKE**               |               **ILIKE**              |
|:------------------------------------:|:------------------------------------:|
| 대소문자를 구분해서 문자열 패턴 비교 | 대소문자를 무시하고 문자열 패턴 비교 |
|                                      | `PostgreSQL` 전용 문법               |

```sql
-- LIKE
SELECT 학생번호, 주소
FROM 학생
WHERE 주소 LIKE '서울%';            -- '서울'로 시작하는 모든 주소

SELECT 학생번호, 이메일
FROM 학생
WHERE 이메일 LIKE '%@gmail.com';   -- gmail 도메인을 사용하는 모든 이메일

SELECT 학생번호, 생년월일
FROM 학생
WHERE 이메일 LIKE '__05%';         -- 3~4번째 글자가 '05'(5월생)인 모든 데이터

-- ILIKE
SELECT 학생번호, 이메일
FROM 학생
WHERE 이메일 LIKE '%@GMAIL.COM';   -- 대소문자 상관없이 '@gmail.com' 검색
```
- 와일드카드 `%`: 글자 수 제한 없는 모든 문자
- 와일드카드 `_`: 언더스코어 1개당 1글자

#### GROUP BY

```sql
SELECT 학과번호,                    
       COUNT(*) AS 학생수          
FROM 학생
GROUP BY 학과번호;                  -- 학과별 학생 수 조회

SELECT 학과번호,                    
       SUM(이수학점) AS 총이수학점
FROM 학생
GROUP BY 학과번호;                  -- 학과별 학생들의 이수학점 총합 조회

SELECT 학과번호,                    
       AVG(평점) AS 학과평점
FROM 학생
GROUP BY 학과번호
ORDER BY 학과평점 DESC;             -- 학과별 학생들의 평균 평점 조회 (학과평점이 높은 순으로 정렬)

SELECT 학과번호, 평점, 학생번호, 성명   
FROM 학생
WHERE (학과번호, 평점) IN (
    SELECT 학과번호, MAX(평점)
    FROM 학생
    GROUP BY 학과번호
);                               -- 학과별 최고 평점과 해당 학생 조회 (서브쿼리 사용)

SELECT MIN(평점) AS 전체최저평점
FROM 학생;                        -- 전체 학생(GROUP BY 생략) 중 최저 평점 하나만 조회
```
- 특정 컬럼의 값이 같은 행들을 하나의 그룹으로 묶어주는 역할
- `AS` 절로 ALIAS(별칭)을 지정하면 결과창에서 훨씬 보기 편하며, `ORDER BY` 절에서도 사용 가능
- 보통 집계 함수와 함께 사용됨(집계 함수들은 보통 NULL 값을 무시하고 계산하는 것 주의)
   - `COUNT()` : 조건에 맞는 행의 개수 계산 (`*`를 쓰면 모든 행의 개수)
   - `SUM()` : 숫자 컬럼의 모든 값의 합계를 계산
   - `AVG()` : 숫자 컬럼의 평균값을 계산
   - `MAX()` : 해당 컬럼의 값 중 최대값 반환 (문자열이나 날짜에도 사용 가능)
   - `MIN()` : 해당 컬럼의 값 중 최소값 반환
- GROUP BY 없이 집계 함수 사용 시 테이블 전체를 하나의 그룹으로 간주

#### HAVING (vs WHERE)

|                              **WHERE**                             |                                 **HAVING**                                 |
|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| GROUP BY하기 전의 개별 행들을 먼저 필터링<br>(집계 함수 사용 불가) | GROUP BY에 의해 그룹화된 결과(집계 값)<br>에 대해 조건을 걸어 필터링 |


```sql
SELECT 학과번호,                -- 평균 평점이 4.0을 넘는 '우수 학과'만 조회
       AVG(평점) AS 학과평점
FROM 학생
GROUP BY 학과번호
HAVING AVG(평점) >= 4.0;       -- HAVING 절에 별칭 직접 사용 불가(MySQL에서는 허용)
```

#### JOIN / UNION

|                      **JOIN**                      |                  **UNION**                  |
|:--------------------------------------------------:|:-------------------------------------------:|
| 서로 다른 테이블의 '관계 있는 정보'를 한 행에 표현 | 구조가 같은 결과들을 하나의 목록으로 합치기 |
| 행을 기준으로 옆에 컬럼을 붙임                 | 결과를 아래로 이어 붙임                |
| ON으로 행 간 관계 정의 필요                  | 관계 정의 불필요                     |
| 결과 컬럼 수 증가 가능                       | 결과 컬럼 수 고정                    |

```sql
-- JOIN 예시 (INNER, LEFT만)
SELECT s.학생번호, s.성명, d.학과명
FROM 학생 s
INNER JOIN 학과 d
ON s.학과번호 = d.학과번호;             -- 정상적으로 학과에 소속된 학생만 조회

SELECT s.학생번호, s.성명, d.학과명
FROM 학생 s
LEFT JOIN 학과 d
ON s.학과번호 = d.학과번호;             -- 모든 학생 조회 (소속 학과 없는 학생은 학과명이 NULL로 표시)
```
- `FROM` 기준테이블 `JOIN` 연결테이블 `ON` 연결조건(이 되는 컬럼)
- `INNER JOIN`
   - ON 조건을 만족하는 행만 결과에 포함
   - 조건을 만족하지 못한 행은 양쪽 모두 제거 (NULL이 생기지 않음)
   - 가장 많이 쓰이는 기본값
- `LEFT JOIN`
   - 기준테이블의 모든 행을 무조건 유지
   - ON 조건을 만족하는 행을 찾지 못하면 연결테이블 쪽 컬럼들만 NULL로 채움
- `RIGHT JOIN`
   - 연결테이블의 모든 행을 무조건 유지
   - ON 조건을 만족하는 행을 찾지 못하면 기준테이블 쪽 컬럼들만 NULL로 채움
   - 실무에서는 테이블 순서를 바꿔 LEFT JOIN으로 대체
- `FULL OUTER JOIN`
   - 양쪽 테이블의 모든 행을 전부 유지
   - 조건을 만족하지 못한 행은 데이터가 없는 쪽 테이블 컬럼을 NULL로 채움
   - PostgreSQL 가능 / MySQL 불가

<br>

```sql
-- UNION 예시 ('학생 이름' 목록과 '교수 이름' 목록을 하나의 컬럼으로 이어 붙이기)
SELECT 성명 FROM 학생          
UNION                        -- 중복된 이름은 1번만 출력 (내부적으로 DISTINCT 적용)
SELECT 교수명 FROM 학과;        

SELECT 성명 FROM 학생          
UNION ALL                    -- 중복 제거없이 행 개수(학생 수 + 교수 수) 유지
SELECT 교수명 FROM 학과;
```
- UNION 사용 조건
   1. 컬럼 개수 동일 (각 SELECT의 출력 컬럼 수가 같아야 함)
   2. 컬럼 순서 동일 (각 SELECT의 n번째 컬럼끼리 결합됨)
   3. 데이터 타입 호환 가능 (변환 불가능하면 실행 오류)
- 중복 제거가 필요 없으면 성능이 좋은 `UNION ALL` 사용을 더 추천

### UPDATE

```sql
UPDATE 학생
SET 평점 = 4.3,           -- 평점, 자격증보유 컬럼의 값 변경
    자격증보유 = TRUE
WHERE 학생번호 = 4762      -- 4762번 학생의 행에만 적용
RETURNING *;
```
- 조건을 지정하지 않으면 모든 행에 적용되기 때문에 항상 WHERE을 함께 사용하기
- `RETURNING`: PostgreSQL 전용 기능으로, 변경된 데이터를 즉시 SELECT한 것처럼 화면에 출력

### DELETE

> FOREIGN KEY 삭제 시 부모 테이블의 데이터가 사라져서 이를 참조하던 자식 테이블이 미아가 되는 상황을 방지하기 위해 ON DELETE 설정 필수

```sql
DELETE FROM 학생
WHERE 학생번호 = 3952      -- 3952번 학생의 행에만 적용
RETURNING *;
```

```sql
DELETE FROM 학생;         -- WHERE 조건 미지정시 모든 행 삭제

TRUNCATE TABLE 학생;      -- DELETE보다 빠르고 sequences(인덱스)까지 모두 삭제
```
- 모든 데이터를 지울 때는 2가지 방법 중 하나 선택

## SubQuery

```sql
SELECT 학생번호, 성명, 평점
FROM 학생
WHERE 평점 > (              -- 전체 학생들의 평균 평점보다 높은 학생만 조회
    SELECT AVG(평점)
    FROM 학생
);
```
- 서브쿼리 결과 -> 단일 값(평균 평점)
- 바깥 쿼리에서 비교 연산자로 비교 가능

```sql
SELECT 학생번호, 성명
FROM 학생
WHERE 학과번호 IN (         -- 실제 존재하는 학과에 소속된 학생만 조회
    SELECT 학과번호
    FROM 학과
);
```
- 서브쿼리 결과 -> 여러 행

```sql
SELECT s.학생번호, s.성명, s.학과번호, s.평점, d.학과평균평점
FROM 학생 s
JOIN (
    SELECT 학과번호,                -- 학과번호, 학과평균평점을 가진 임시 테이블
           AVG(평점) AS 학과평균평점
    FROM 학생
    GROUP BY 학과번호
) d ON s.학과번호 = d.학과번호
WHERE s.평점 < d.학과평균평점;        -- 학과별 평균 평점보다 낮은 학생만 조회 

```
- 서브쿼리 결과 -> 임시 테이블
- FROM 절에서 학생 테이블과 임시 테이블을 JOIN

```sql
SELECT d.학과번호, d.학과명
FROM 학과 d
WHERE EXISTS (      -- 학생이 1명이라도 존재하는 학과만 조회
    SELECT 1    -- 더미 값(실제 컬럼 값이 필요 없음을 의미)
    FROM 학생 s
    WHERE s.학과번호 = d.학과번호
);

SELECT d.학과번호, d.학과명
FROM 학과 d
WHERE NOT EXISTS (  -- 반대로 학생이 1명도 없는 학과만 조회
    SELECT 1
    FROM 학생 s
    WHERE s.학과번호 = d.학과번호
);
```
- `EXISTS`는 값이 아니라 행이 하나라도 존재하는지만 검사    
(만족하는 첫 행 발견 시 바로 TRUE 반환, 하나도 없을 경우 FALSE)

## SQL Functions

### string

```sql
-- UPPER: 대문자로 통일 / LOWER: 소문자로 통일
SELECT UPPER(교수_성), LOWER(교수_이름)
FROM 교수;

-- CONCAT: 문자열 합치기
SELECT CONCAT(교수_성, ' ', 교수_이름) AS 교수_fullname
FROM 교수;

-- SUBSTRING: 문자열 일부 추출 (문자열 FROM 시작위치 FOR 길이)
-- POSITION: 부문 문자열의 시작 위치 반환
-- (⚠️ 둘 다 시작 인덱스가 1 !)
SELECT SUBSTRING(이메일 FROM 1 FOR POSITION('@' IN 이메일) - 1) AS 이메일_ID
FROM 학생;

-- REPLACE: 문자열 대체
SELECT REPLACE(이메일, '@univ.com', '@univ.org')
FROM 학생;

-- TRIM: 문자열 앞과 뒤의 공백 제거
SELECT LOWER(TRIM(이메일)) AS 이메일_정규화
FROM 학생;
```

### numeric

```sql
-- ROUND() — Round a number
SELECT ROUND(rental_rate, 0)
FROM film;

-- CEIL() / FLOOR() — Next or lower integer
SELECT CEIL(amount), FLOOR(amount)
FROM payment
LIMIT 5;

-- ABS() — Absolute value
SELECT ABS(-10);

-- POWER()
SELECT POWER(2, 3);  -- 2^3 = 8

-- RANDOM()
SELECT RANDOM();
```

### date/time

```sql
-- NOW() — Current timestamp
SELECT NOW();

-- CURRENT_DATE
SELECT CURRENT_DATE;

-- AGE() — Difference between two timestamps
SELECT AGE(NOW(), rental_date)
FROM rental
LIMIT 5;

-- DATE_TRUNC() — Truncate timestamps (very important)
SELECT DATE_TRUNC('month', rental_date)
FROM rental
LIMIT 5;

-- EXTRACT() — Pull out year, month, day
SELECT EXTRACT(YEAR FROM rental_date) AS year
FROM rental
LIMIT 5;
```

### conditional

```sql
-- COALESCE() — Replace NULLs
SELECT COALESCE(email, 'no email') AS email_info
FROM customer;

-- NULLIF() — Return NULL if values equal
SELECT NULLIF(amount, 0)
FROM payment;

-- CASE WHEN — Conditional logic
SELECT 
    amount,
    CASE 
        WHEN amount > 5 THEN 'High'
        ELSE 'Low'
    END AS payment_size
FROM payment;

```

### aggregate

[↑ **GROUP BY**에서 참고](#)

### postgresql special

```sql
-- STRING_AGG() — combine values into one string
SELECT STRING_AGG(first_name, ', ')
FROM customer
WHERE store_id = 1;

-- GENERATE_SERIES() — create rows on the fly
SELECT generate_series(1, 10);

-- Generate one date per day for a month
SELECT generate_series(
    '2025-01-01'::date,
    '2025-01-31'::date,
    '1 day'::interval
);

-- Every hour today
SELECT generate_series(
    NOW()::date,
    NOW()::date + 1,
    '1 hour'
);

-- TO_CHAR() — Format numbers and dates
SELECT TO_CHAR(payment_date, 'YYYY-MM-DD')
FROM payment
LIMIT 5;

-- TO_DATE() — convert text to date
SELECT TO_DATE('2025-02-01', 'YYYY-MM-DD');
```



----
```sql

```
----
