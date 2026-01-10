---
excerpt: "미리보기"
title: "SQL"
header:
  teaser: "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/SQL-Products-Option-Light_v1_RE4xfAg?resMode=sharp2&op_usm=1.5,0.65,15,0&wid=610&qlt=100&fmt=png-alpha&fit=constrain"
categories:
  - SQL
tags:
last_modified_at: YYYY-MM-DDT00:30:30+09:00
---

## Install & Setting

Docker 기반 PostgreSQL + DBeaver 설정 (macOS)

1. **설치**
   - Docker Desktop
      - PostgreSQL 컨테이너 실행 환경
      - 컨테이너 상태 / 로그 확인용 GUI
   - DBeaver
      - DB 접속
      - 스키마·테이블 시각화
      - SQL 쿼리 실행
2. **Docker Desktop 실행**
   - 메뉴바의 🐳 아이콘이 Running 상태인지 확인
   - Docker 엔진이 실행된 상태에서만 PostgreSQL 컨테이너를 생성·실행할 수 있음
3. **프로젝트 디렉토리 구성**
    ```text
    project-root/
    ├─ docker-compose.yml     <- PostgreSQL 서버 설정
    └─ init/                  <- DB 초기화 SQL (번호를 붙여서 관리 가능)
        ├─ 01_schema.sql
        ├─ 02_data.sql
    ```
4. **docker-compose.yml 작성** (서버 설정)
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
5. **프로젝트 디렉토리에서 컨테이너 실행**
   - DB 컨테이너 실행
    ```bash
    docker compose up -d
    ```
    `-d`: 백그라운드 실행(권장)
   - DB 컨테이너 중지 및 삭제
    ```bash
    docker compose down
    ```
    `-v`: 볼륨까지 삭제하는 옵션 → DB 완전 초기화      
    (SQL 파일 변경 후 처음부터 다시 적용하고 싶을 때 사용)
6. **DBeaver로 DB 접속**
   - 첫 실행 시 `New Database Connection`으로 연결
      - Driver: `PostgreSQL`
      - Connection Settings:
         - Connect by: `Host`
         - Host: `localhost`
         - Database, Port, Username, Password → `docker-compose.yml`의 값과 동일

## SQL Query



---


# create db
CREATE DATABASE company;

# create schema
CREATE SCHEMA hr;

# change search path
SET search_path TO hr;

# create table
CREATE TABLE hr.employees (
    id SERIAL PRIMARY KEY,
    name TEXT,
    position TEXT
);

# insert data
INSERT INTO hr.employees (name, position)
VALUES ('Alice', 'Manager');

# query with schema
SELECT * FROM hr.employees;


## SELECT

SET search_path to dvdrental;

SELECT column1, column2, ...
FROM table_name;

SELECT first_name, last_name 
FROM actor;

# ORDER BY – Sorting results
SELECT first_name, last_name, actor_id
FROM actor
ORDER BY actor_id DESC;

# WHERE – Filtering rows
SELECT title, length
FROM film
WHERE length > 100;

SELECT title, length, rating
FROM film
WHERE length > 100 AND rating = 'G';

# LIMIT – Restrict number of rows
SELECT title, length
FROM film
LIMIT 10;

# DISTINCT – Remove duplicates
SELECT DISTINCT(rental_rate)
FROM film;

# BETWEEN — Range filtering
SELECT title, length
FROM film
WHERE length BETWEEN 50 AND 100;

SELECT title, length
FROM film
WHERE length >= 50 AND length <= 100;

# IN — Multiple exact values
SELECT title, rating
FROM film
WHERE rating IN ('PG', 'G', 'PG-13');

SELECT title, rating
FROM film
WHERE rating = 'PG' OR rating = 'G' OR rating = 'PG-13';

# LIKE — Pattern matching (case-sensitive)
SELECT title, rating
FROM film
WHERE title LIKE 'AC%';

SELECT title, rating
FROM film
WHERE title LIKE '%EGG';

SELECT title, rating
FROM film
WHERE title LIKE '%EGG%';

SELECT title, rating
FROM film
WHERE title LIKE 'SPY_____'; # 8 letter words starting with SPY

# ILIKE — Case-insensitive pattern matching (PostgreSQL only)
SELECT title, rating
FROM film
WHERE title ILIKE '%egg%';


## Set default search_path for a specific database

ALTER DATABASE dvdrental SET search_path TO dvdrental;
SHOW search_path;


## GROUP BY

SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC;

SELECT customer_id,
       SUM(amount) AS total_paid
FROM payment
GROUP BY customer_id
ORDER BY total_paid DESC
LIMIT 10;

SELECT rating,
       AVG(rental_duration) AS avg_rental_days
FROM film
GROUP BY rating;

SELECT rating, MAX(rental_duration)
FROM film
GROUP BY rating;

SELECT MIN(rental_duration)
FROM film;

SELECT MAX(rental_duration)
FROM film;


## HAVING

SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
HAVING COUNT(*) > 200;

SELECT customer_id, SUM(amount) AS total_paid
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100;

SELECT rating, AVG(rental_duration) AS avg_duration
FROM film
GROUP BY rating
HAVING AVG(rental_duration) > 5;


## JOIN & UNION

SELECT f.title, COUNT(*)
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title;

SELECT f.title, i.inventory_id
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id;

SELECT f.title, r.rental_id
FROM film f
FULL OUTER JOIN inventory i ON f.film_id = i.film_id
FULL OUTER JOIN rental r ON i.inventory_id = r.inventory_id;

SELECT first_name FROM customer
UNION
SELECT first_name FROM actor
ORDER BY first_name;

SELECT first_name FROM customer
UNION ALL
SELECT first_name FROM actor
ORDER BY first_name;


## Insert

INSERT INTO actor (first_name, last_name)
VALUES ('John', 'Wick');

INSERT INTO actor (first_name, last_name)
VALUES
  ('Amy', 'Smith'),
  ('Bob', 'Johnson'),
  ('Charlie', 'Lee');

SELECT address_id, address, district
FROM address
LIMIT 5;

INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date)
VALUES (
  1,
  'Joon',
  'Lee',
  'joon@example.com',
  (SELECT address_id FROM address LIMIT 1),  -- pick any existing address
  1,
  NOW()
);


## Update

UPDATE customer
SET email = 'new_email@example.com'
WHERE customer_id = 1;

UPDATE customer
SET first_name = 'MARY',
    last_name  = 'SMITH',
    email      = 'MARY.SMITH@sakilacustomer.org'
WHERE customer_id = 1;

UPDATE film
SET rental_rate = rental_rate + 1.00
WHERE rating = 'PG';

UPDATE customer
SET activebool = FALSE;

UPDATE customer
SET first_name = 'MARY'
WHERE customer_id = 1
RETURNING *;


## Delete

DELETE FROM customer
WHERE customer_id = 1;

DELETE FROM payment
WHERE amount < 1.00;

DELETE FROM customer;

TRUNCATE TABLE customer;

DELETE FROM customer
WHERE customer_id = 10
RETURNING *;

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    amount NUMERIC(5,2),
    payment_date TIMESTAMP,
    FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
        ON DELETE CASCADE
);

ALTER TABLE payment
ADD CONSTRAINT fk_payment_customer
FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
    ON DELETE CASCADE;


## Alter table

ALTER TABLE customer
ADD COLUMN middle_name VARCHAR(50);

ALTER TABLE customer
ADD COLUMN vip BOOLEAN DEFAULT FALSE;

ALTER TABLE customer
RENAME COLUMN vip TO very_important_person;

ALTER TABLE customer
ALTER COLUMN very_important_person DROP DEFAULT;

ALTER TABLE customer
ALTER COLUMN very_important_person TYPE INTEGER
USING very_important_person::int;

ALTER TABLE customer
ALTER COLUMN very_important_person TYPE INTEGER
USING CASE
        WHEN very_important_person = 'true' THEN 1
        WHEN very_important_person = 'false' THEN 0
     END;

ALTER TABLE customer
ALTER COLUMN middle_name SET DEFAULT 'NA';

ALTER TABLE customer
ALTER COLUMN middle_name DROP DEFAULT;

ALTER TABLE customer
ALTER COLUMN email SET NOT NULL

ALTER TABLE customer
ALTER COLUMN email DROP NOT NULL;

ALTER TABLE customer
DROP COLUMN middle_name;

ALTER TABLE customer
DROP COLUMN very_important_person;


# The following SQL may break the tables - DO NOT RUN

# Add a Primary Key
ALTER TABLE actor
ADD CONSTRAINT actor_pkey PRIMARY KEY (actor_id);

# Add a Foreign Key
ALTER TABLE payment
ADD CONSTRAINT payment_customer_fkey
FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
    ON DELETE CASCADE;

# Add UNIQUE
ALTER TABLE customer
ADD CONSTRAINT customer_email_key UNIQUE (email);

# Drop the key
ALTER TABLE payment
DROP CONSTRAINT payment_customer_fkey;

# Rename the table
ALTER TABLE customer
RENAME TO client;


## SubQuery

SELECT customer_id, amount
FROM payment
WHERE amount > (
    SELECT AVG(amount)
    FROM payment
);

SELECT customer_id, first_name, last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM rental
);

SELECT customer_id,
       (SELECT COUNT(*)
        FROM rental r
        WHERE r.customer_id = c.customer_id) AS rental_count
FROM customer c;

SELECT customer_id, total_paid
FROM (
    SELECT customer_id, SUM(amount) AS total_paid
    FROM payment
    GROUP BY customer_id
) AS summary
WHERE total_paid > 50;

# Customers who have rentals
SELECT c.customer_id, c.first_name, c.last_name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM rental r
    WHERE r.customer_id = c.customer_id
);

# Customers who don’t have rentals
SELECT c.customer_id
FROM customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM rental r
    WHERE r.customer_id = c.customer_id
);

INSERT INTO actor (first_name, last_name)
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'A%';

UPDATE customer c
SET active = 0
WHERE NOT EXISTS (
    SELECT 1
    FROM rental r
    WHERE r.customer_id = c.customer_id
);

DELETE FROM customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM rental r
    WHERE r.customer_id = c.customer_id
);


## SQL functions

# String Functions
-- UPPER() / LOWER() — Change case
SELECT UPPER(first_name), LOWER(last_name)
FROM customer
LIMIT 5;

-- CONCAT() — Combine strings
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customer;

-- SUBSTRING() — Extract text
SELECT SUBSTRING(email FROM 1 FOR 5)
FROM customer;

-- REPLACE() — Replace text
SELECT REPLACE(email, '@sakilacustomer.org', '@example.com')
FROM customer;

-- TRIM() — Remove leading/trailing spaces
SELECT TRIM('   hello   ');

# Numeric Functions
-- ROUND() — Round a number
SELECT ROUND(rental_rate, 0)
FROM film;

-- CEIL() / FLOOR() — Next or lower integer
SELECT CEIL(amount), FLOOR(amount)
FROM payment
LIMIT 5;

-- ABS() — Absolute value
SELECT ABS(-10);

# Date & Time Functions
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

# Aggregate Functions
-- COUNT()
SELECT COUNT(*) FROM customer;

-- SUM()
SELECT SUM(amount) AS total_revenue
FROM payment;

-- AVG()
SELECT AVG(rental_rate)
FROM film;

-- MAX() / MIN()
SELECT MAX(amount), MIN(amount)
FROM payment;

# Conditional Functions
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

# Mathematical Functions
-- POWER()
SELECT POWER(2, 3);  -- 2^3 = 8

-- RANDOM()
SELECT RANDOM();

# Useful PostgreSQL-Specific Functions
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


## CTE

WITH customer_spending AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        SUM(p.amount) AS total_spent
    FROM customer c
    JOIN payment p ON c.customer_id = p.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name
)
SELECT *
FROM customer_spending
WHERE total_spent >
    (SELECT AVG(total_spent) FROM customer_spending)
ORDER BY total_spent DESC;


WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT * FROM numbers;


EXPLAIN (ANALYZE, BUFFERS)
WITH pr AS MATERIALIZED (
  SELECT p.amount, r.rental_date
  FROM payment p
  JOIN rental r ON r.rental_id = p.rental_id
)
SELECT
  (SELECT sum(amount) FROM pr
   WHERE rental_date >= DATE '2005-05-01' AND rental_date < DATE '2005-06-01') AS may_sum,
  (SELECT sum(amount) FROM pr
   WHERE rental_date >= DATE '2005-06-01' AND rental_date < DATE '2005-07-01') AS jun_sum;


EXPLAIN (ANALYZE, BUFFERS)
WITH pr AS NOT MATERIALIZED (
  SELECT p.amount, r.rental_date
  FROM payment p
  JOIN rental r ON r.rental_id = p.rental_id
)
SELECT
  (SELECT sum(amount) FROM pr
   WHERE rental_date >= DATE '2005-05-01' AND rental_date < DATE '2005-06-01') AS may_sum,
  (SELECT sum(amount) FROM pr
   WHERE rental_date >= DATE '2005-06-01' AND rental_date < DATE '2005-07-01') AS jun_sum;


## CASE WHEN

SELECT amount,
       CASE
           WHEN amount >= 5 THEN 'High'
           ELSE 'Low'
       END AS payment_level
FROM payment;

SELECT title,
    CASE
	   WHEN length < 60 THEN 'Short'
	   WHEN length BETWEEN 60 AND 120 THEN 'Medium'
	   ELSE 'Long'
    END AS film_length
FROM film;

SELECT first_name,
    CASE
        WHEN email IS NULL THEN 'No Email'
        ELSE email
    END AS email_status
FROM customer;

SELECT
  CASE
      WHEN email IS NULL THEN 'missing'
      WHEN email = '' THEN 'empty'
      ELSE 'present'
  END AS email_state
FROM customer;

SELECT
    SUM(CASE WHEN active = 1 THEN 1 ELSE 0 END) AS active_count,
    SUM(CASE WHEN active = 0 THEN 1 ELSE 0 END) AS inactive_count
FROM customer;

SELECT *
FROM payment
WHERE
  CASE
      WHEN amount > 5 THEN 1
      ELSE 0
  END = 1;

# be careful
UPDATE customer
SET active = CASE
                WHEN last_update < NOW() - INTERVAL '5 years' THEN 0
                ELSE active
             END;

SELECT
    customer_id,
    SUM(CASE WHEN amount < 5 THEN amount ELSE 0 END) AS small_payments,
    SUM(CASE WHEN amount >= 5 THEN amount ELSE 0 END) AS large_payments
FROM payment
GROUP BY customer_id;



```python

```
<i class="fa-solid fa-right-from-bracket"></i> <pre></pre>

<br><br>