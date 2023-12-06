drop table if exists groups CASCADE;
CREATE TABLE groups (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

drop table if exists students CASCADE;
CREATE TABLE students (
id SERIAL PRIMARY KEY,
full_name VARCHAR(150) NOT NULL,
group_id INTEGER REFERENCES groups(id)
);

drop table if exists teachers CASCADE;
CREATE TABLE teachers (
id SERIAL PRIMARY KEY,
full_name VARCHAR(150) NOT NULL
);

drop table if exists subjects CASCADE;
CREATE TABLE subjects (
id SERIAL PRIMARY KEY,
name VARCHAR(150) NOT NULL,
teacher_id INTEGER REFERENCES teachers(id)
);

drop table if exists grades CASCADE;
CREATE TABLE grades (
id SERIAL PRIMARY KEY,
student_id INTEGER REFERENCES students(id),
subject_id INTEGER REFERENCES subjects(id),
grade INTEGER CHECK (grade >= 0 AND grade <= 100),
grade_date DATE NOT NULL
);

SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;

SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;