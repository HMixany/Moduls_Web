SELECT
    AVG(grade) AS AverageGrade
FROM
    grades;

SELECT
    teachers.full_name AS TeacherName,
    subjects.name AS CourseName
FROM
    teachers
JOIN subjects ON teachers.id = subjects.teacher_id
ORDER BY
    TeacherName, CourseName;
   
SELECT
    groups.name AS GroupName,
    students.full_name AS StudentName
FROM
    groups
JOIN students ON groups.id = students.group_id
ORDER BY
    GroupName, StudentName;

SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;

select groups.name AS GroupName, ROUND(AVG(g.grade), 2) AS AverageGrade
from grades g
JOIN students s ON g.student_id = s.id
JOIN groups ON s.group_id = groups.id
where g.subject_id = 1
GROUP by groups.name
ORDER by groups.name;

select s.full_name AS StudentName
from groups g
JOIN students s ON g.id = s.group_id
where g.id = 1
ORDER BY StudentName;

select s.full_name AS StudentName, grades.grade AS Grade, subjects.name  as SubjectName
from students s
JOIN grades ON s.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON s.group_id = groups.id
where groups.id  = 1 AND subjects.id  = 1
ORDER by StudentName;

SELECT teachers.full_name AS TeacherName, subjects.name AS CourseName
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
WHERE teachers.id = 1
ORDER BY TeacherName, CourseName;

select t.full_name AS TeacherName, subjects.name AS SubjectName, AVG(grades.grade) AS AverageGrade
from teachers t
JOIN subjects ON t.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
where t.id = 1
GROUP by t.full_name, subjects.name
ORDER by TeacherName, SubjectName;

select students.full_name AS StudentName, subjects.name AS CourseName
from students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
where students.id  = 1
ORDER by CourseName;

SELECT distinct students.full_name AS StudentName, subjects.name AS CourseName
from students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
where students.id = 1
ORDER by CourseName;

select distinct subjects.name AS CourseName
from students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
where students.id = 1 AND teachers.id = 1
ORDER by CourseName;


