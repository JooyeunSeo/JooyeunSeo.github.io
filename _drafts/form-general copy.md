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

1. `FROM`      : 어떤 테이블에서 데이터를 가져올지 결정 (+ JOIN 절도 함께 실행)
2. `WHERE`     : 개별 행을 조건에 맞게 먼저 필터링
3. `GROUP BY`  : 남은 행들을 특정 컬럼 기준으로 그룹화 (집계 함수는 그룹화 후 사용)
4. `HAVING`    : 그룹화된 결과물 중에서 조건에 맞는 그룹만 다시 필터링
5. `SELECT`    : 출력할 컬럼 선택 및 별칭 부여
6. `DISTINCT`  : 중복된 행을 하나로 병합
7. `ORDER BY`  : 모든 결과가 나온 뒤 마지막으로 정렬 (별칭 사용 가능)
8. `LIMIT`     : 정렬된 결과의 최상단부터 필요한 만큼만 잘라서 출력

<br>

## Data Definition

### CREATE Table

```sql
CREATE TABLE academic.학과 (
    학과번호 INT PRIMARY KEY,       -- 컬럼명 컬럼타입 나열
    학과명 TEXT
);

CREATE TABLE academic.수강생 (
    수강생번호 SERIAL PRIMARY KEY,   -- PRIMARY KEY
    성명 TEXT,
    학과명 TEXT,
    평점 FLOAT,
    이수학점 INT,
    자격증보유 BOOLEAN,
    생년월일 TEXT,
    주소 TEXT,
    이메일 TEXT UNIQUE,
    학과번호 INT,
    FOREIGN KEY (학과번호)          -- FOREIGN KEY
        REFERENCES 학과(학과번호)
        ON DELETE SET NULL
);
```
- `SERIAL`은 내부적으로 INT + SEQUENCE 성질을 지니고 있어 자동으로 숫자가 증가
- `UNIQUE`는 중복 데이터를 비허용하는 옵션
- `PRIMARY KEY` : 행을 유일하게 식별하는 키로, 중복 불가 + NULL 불가
- `FOREIGN KEY` : 수강생 테이블의 **학과번호** 컬럼은 반드시 다른 테이블(학과)에 존재해야 외래키로 사용 가능

### ALTER Table

#### ADD Column

```sql
ALTER TABLE 수강생
ADD COLUMN 성별 INT;             -- 남자는 1, 여자는 2로 저장되는 컬럼
```

#### DROP Column

```sql
ALTER TABLE 수강생
DROP COLUMN 학과명;
```

#### change Column Type

```sql
-- PostgreSQL 전용 문법 (:: 연산자 사용)
ALTER TABLE 학생
ALTER COLUMN 성별 TYPE TEXT     -- 기존 INT 타입 데이터를 TEXT 타입으로 변경
USING 성별::TEXT;               -- 1, 2를 '1', '2'로 강제 형변환 (USING절 필요)

-- 표준 SQL 문법 (CAST 함수 사용)
ALTER TABLE 학생
ALTER COLUMN 성별 TYPE TEXT
USING CAST(성별 AS TEXT);
```

```sql
ALTER TABLE 수강생
ALTER COLUMN 성별 TYPE TEXT
USING (CASE 성별                -- 데이터 재배치 (1 -> '남', 2 -> '여')
           WHEN 1 THEN '남'
           WHEN 2 THEN '여'
           ELSE '미지정'
       END);
```

#### change Table Name

```sql
ALTER TABLE 수강생
RENAME TO 학생;
```

#### change Column Name

```sql
ALTER TABLE 학생
RENAME COLUMN 수강생번호 TO 학생번호;
```

<br>

| 기능           | 표준 SQL / PostgreSQL 문법                                           | MySQL 전용 문법                       |
|--------------|---------------------------------------------------------------------|--------------------------------------|
| 타입 변경      | `ALTER` COLUMN 성별 `TYPE` TEXT                                      | `MODIFY` COLUMN 성별 VARCHAR(10)      |
| 이름+타입 변경 | `RENAME` COLUMN 성별 `TO` gender<br>`ALTER` COLUMN gender `TYPE` TEXT | `CHANGE` COLUMN 성별 gender VARCHAR(10) |

<br>

## Data Manupulation

### INSERT (create)
Single row

Multiple rows

INSERT FROM SELECT

이부분은 
INSERT INTO hr.employees (name, position)
VALUES ('Alice', 'Manager');
이런식으로 예시가 필요

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

#### LIKE 

```sql
SELECT 학생번호, 주소
FROM 학생
WHERE 주소 LIKE '서울%';                -- '서울'로 시작하는 모든 주소

SELECT 학생번호, 이메일
FROM 학생
WHERE 이메일 LIKE LIKE '%@gmail.com';   -- gmail 도메인을 사용하는 모든 이메일

SELECT 학생번호, 생년월일
FROM 학생
WHERE 이메일 LIKE LIKE '__05%';         -- 3~4번째 글자가 '05'(5월생)인 모든 데이터
```
- 문자열 패턴 비교 (대소문자 구분)
- 와일드카드:
   - `%`: 글자 수 제한 없는 모든 문자
   - `_`: 언더스코어 1개당 1글자

#### ILIKE 

```sql
SELECT 학생번호, 이메일
FROM 학생
WHERE 이메일 LIKE LIKE '%@GMAIL.COM';   -- 대소문자 상관없이 '@gmail.com' 검색
```
- 문자열 패턴 비교 (대소문자 무시)
- `PostgreSQL` 전용 문법

#### GROUP BY (+ Aggregation Function)

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
- 자주 사용되는 집계 함수 (Aggregation Function)
   - `COUNT()` : 조건에 맞는 행의 개수 계산 (`*`를 쓰면 모든 행의 개수)
   - `SUM()` : 숫자 컬럼의 모든 값의 합계를 계산
   - `AVG()` : 숫자 컬럼의 평균값을 계산
   - `MAX()` : 해당 컬럼의 값 중 최대값 반환 (문자열이나 날짜에도 사용 가능)
   - `MIN()` : 해당 컬럼의 값 중 최소값 반환
- 집계 함수들은 보통 NULL 값을 무시하고 계산
- GROUP BY 없이 집계 함수 사용 시 테이블 전체를 하나의 그룹으로 간주

#### HAVING (vs WHERE)

- `WHERE`: 그룹화하기 전의 개별 행들을 먼저 필터링(집계 함수 사용 불가)
- `HAVING`: **GROUP BY**에 의해 그룹화된 결과(집계 값)에 대해 조건을 걸어 필터링

```sql
SELECT 학과번호,                -- 평균 평점이 4.0을 넘는 '우수 학과'만 조회
       AVG(평점) AS 학과평점
FROM 학생
GROUP BY 학과번호
HAVING AVG(평점) >= 4.0;       -- HAVING 절에 별칭 직접 사용 불가(MySQL에서는 허용)
```






### UPDATE
UPDATE ... SET ... WHERE ...

UPDATE with subquery

UPDATE ... RETURNING

### DELETE
DELETE with condition

DELETE with subquery

TRUNCATE

DELETE ... RETURNING




----
```sql

```
----



<i class="fa-solid fa-right-from-bracket"></i> <pre></pre>

<br><br>