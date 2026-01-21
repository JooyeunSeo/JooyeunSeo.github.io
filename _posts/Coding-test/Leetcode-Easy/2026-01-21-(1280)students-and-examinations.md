---
excerpt: "'LeetCode: Students and Examinations' 풀이 정리"
title: "\01280. Students and Examinations"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Database
  - Pandas
  - SQL
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})
```
<br>

Table: `Students`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
</pre>

Table: `Subjects`
<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
</pre>

Table: `Examinations`
<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
</pre>

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Students table:
    +------------+--------------+
    | student_id | student_name |
    +------------+--------------+
    | 1          | Alice        |
    | 2          | Bob          |
    | 13         | John         |
    | 6          | Alex         |
    +------------+--------------+
    Subjects table:
    +--------------+
    | subject_name |
    +--------------+
    | Math         |
    | Physics      |
    | Programming  |
    +--------------+
    Examinations table:
    +------------+--------------+
    | student_id | subject_name |
    +------------+--------------+
    | 1          | Math         |
    | 1          | Physics      |
    | 1          | Programming  |
    | 2          | Programming  |
    | 1          | Physics      |
    | 1          | Math         |
    | 13         | Math         |
    | 13         | Programming  |
    | 13         | Physics      |
    | 2          | Math         |
    | 1          | Math         |
    +------------+--------------+
    </pre>
- Output:    
    <pre>
    +------------+--------------+--------------+----------------+
    | student_id | student_name | subject_name | attended_exams |
    +------------+--------------+--------------+----------------+
    | 1          | Alice        | Math         | 3              |
    | 1          | Alice        | Physics      | 2              |
    | 1          | Alice        | Programming  | 1              |
    | 2          | Bob          | Math         | 1              |
    | 2          | Bob          | Physics      | 0              |
    | 2          | Bob          | Programming  | 1              |
    | 6          | Alex         | Math         | 0              |
    | 6          | Alex         | Physics      | 0              |
    | 6          | Alex         | Programming  | 0              |
    | 13         | John         | Math         | 1              |
    | 13         | John         | Physics      | 1              |
    | 13         | John         | Programming  | 1              |
    +------------+--------------+--------------+----------------+
    </pre>
- Explanation:        
The result table should contain all students and all subjects.      
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.      
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.      
Alex did not attend any exams.      
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # 모든 학생-과목 조합 생성
    student_subject = students.merge(subjects, how='cross')

    # 시험 참가 기록 카운트
    exam_attend = examinations.assign(attended=1)

    # left join
    student_exam = student_subject.merge(exam_attend, on=['student_id', 'subject_name'], how='left')

    # 그룹핑 + 카운트
    count_attend = (student_exam
        .groupby(['student_id', 'student_name', 'subject_name'], dropna=False)['attended']
        .count()
        .reset_index(name='attended_exams')
    )
    
    return count_attend
```
<i class="fa-solid fa-clock"></i> Runtime: **325** ms \| Beats **96.13%**    
<i class="fa-solid fa-memory"></i> Memory: **68.57** MB \| Beats **86.34%**    

시험을 치지 않은 학생도 attended_exams 컬럼값을 0으로 설정해야하기 때문에 시험 참가 기록을 카운트하는 컬럼을 새로 생성했다. 이후 테이블을 merge할 때 존재하지 않는 학생-과목 조합의 attended는 0이 된다.     
또 주의해야 할 예시는 학생 이름이 NaN값인 경우에도 행을 유지해야 하는 경우인데, groupby할 때 dropna를 하지 못하도록 설정하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/students-and-examinations/solutions/5874925/real-explained-step-by-step-1250-all-sql-51z7/" target="_blank">1st</a>

```sql
SELECT
    S.student_id,
    S.student_name,
    SU.subject_name,
    COUNT(E.student_id) attended_exams
FROM Students S CROSS JOIN Subjects SU
LEFT JOIN Examinations E
    ON S.student_id = E.student_id AND SU.subject_name = E.subject_name
GROUP BY S.student_id, S.student_name, SU.subject_name
ORDER BY S.student_id, S.student_name, SU.subject_name
;
```
판다스와 같은 흐름

### <a href="https://leetcode.com/problems/students-and-examinations/solutions/3511410/mysql-three-solutions-by-bhagyeshakkar-k71e/" target="_blank">2nd</a>

```sql
SELECT s.student_id, s.student_name, sub.subject_name, COALESCE(e.attended_exams, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
ORDER BY s.student_id, sub.subject_name;
```
서브쿼리를 사용하는 방법