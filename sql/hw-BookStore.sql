CREATE DATABASE BookStore;
USE BookStore;

CREATE TABLE IF NOT EXISTS Authors (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    AuthorID INTEGER,
    Price REAL,
);

INSERT INTO Authors (FirstName, LastName) VALUES 
('Лев', 'Толстой'),
('Фёдор', 'Достоевский');

INSERT INTO Books (Title, AuthorID, Price) VALUES 
('Война и мир', 1, 100.00),
('Анна Каренина', 1, 200.00);

DELETE FROM Books;

DELETE FROM Authors;