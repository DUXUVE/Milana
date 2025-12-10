CREATE DATABASE IF NOT EXISTS Student;
USE Student;

CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL,
    enrollment_date TEXT NOT NULL
);

INSERT INTO Students (name, birth_date, email, course_name, enrollment_date) VALUES
('Иван Иванов', '2000-05-15', 'ivan@example.com', 'Программирование', '2024-09-01'),
('Мария Петрова', '2001-03-22', 'maria@example.com', 'Математика', '2024-09-01'),
('Алексей Сидоров', '1999-11-30', 'alex@example.com', 'Программирование', '2024-09-15');

SELECT * 
FROM Students 
WHERE course_name IN (
    SELECT course_name 
    FROM Students 
    WHERE course_name = 'Программирование'
);