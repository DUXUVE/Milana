CREATE TABLE "volieres" (
    "id" BIGSERIAL PRIMARY KEY,
    "status" VARCHAR(50) NOT NULL,
    "last_clean" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "employees" (
    "id" BIGSERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "role" VARCHAR(50) NOT NULL
);

CREATE TABLE "animals" (
    "id" BIGSERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "age" INTEGER NOT NULL CHECK ("age" >= 0),
    "voliere_id" BIGINT NOT NULL REFERENCES "volieres"("id")
);

CREATE TABLE "cleanings" (
    "id" BIGSERIAL PRIMARY KEY,
    "date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "employee_id" BIGINT NOT NULL REFERENCES "employees"("id"),
    "voliere_id" BIGINT NOT NULL REFERENCES "volieres"("id")
);

CREATE TABLE "feedings" (
    "id" BIGSERIAL PRIMARY KEY,
    "date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "animal_id" BIGINT NOT NULL REFERENCES "animals"("id"),
    "employee_id" BIGINT NOT NULL REFERENCES "employees"("id")
);

CREATE TABLE "animal_employee_responsibles" (
    "id" BIGSERIAL PRIMARY KEY,
    "animal_id" BIGINT NOT NULL REFERENCES "animals"("id"),
    "employee_id" BIGINT NOT NULL REFERENCES "employees"("id"),
    "date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE ("animal_id", "employee_id")
);

-- Вставка данных в volieres
INSERT INTO "volieres" ("status", "last_clean") VALUES
('active', '2026-07-01 10:00:00'),
('active', '2026-07-02 11:30:00'),
('maintenance', '2026-06-28 09:00:00'),
('active', '2026-07-03 14:00:00'),
('active', '2026-07-04 08:30:00'),
('closed', '2026-06-25 16:00:00'),
('active', '2026-07-05 12:00:00'),
('active', '2026-07-06 10:30:00'),
('maintenance', '2026-06-30 15:00:00'),
('active', '2026-07-07 09:30:00');

-- Вставка данных в employees
INSERT INTO "employees" ("name", "role") VALUES
('Иванов Иван', 'zookeeper'),
('Петрова Анна', 'veterinarian'),
('Сидоров Петр', 'cleaner'),
('Козлова Мария', 'zookeeper'),
('Новиков Алексей', 'veterinarian'),
('Морозова Елена', 'cleaner'),
('Волков Дмитрий', 'zookeeper'),
('Лебедева Ольга', 'cleaner'),
('Соколов Андрей', 'veterinarian'),
('Попова Татьяна', 'zookeeper');

-- Вставка данных в animals
INSERT INTO "animals" ("name", "age", "voliere_id") VALUES
('Лев Симба', 5, 1),
('Тигр Шерхан', 7, 1),
('Слон Джамбо', 12, 2),
('Жираф Мелман', 8, 2),
('Зебра Марти', 4, 3),
('Обезьяна Кинг', 6, 3),
('Медведь Балу', 9, 4),
('Волк Акела', 5, 4),
('Панда По', 3, 5),
('Кенгуру Рокки', 4, 5),
('Лиса Алиса', 2, 6),
('Заяц Багз', 1, 6),
('Орел Сокол', 10, 7),
('Попугай Кеша', 15, 7),
('Пингвин Пинго', 6, 8),
('Тюлень Немо', 3, 8),
('Крокодил Гена', 20, 9),
('Бегемот Мотя', 11, 9),
('Рысь Мурка', 4, 10),
('Ежик Соник', 2, 10);

-- Вставка данных в cleanings (множество записей для разных сотрудников и вольеров)
INSERT INTO "cleanings" ("date", "employee_id", "voliere_id") VALUES
('2026-07-01 08:00:00', 3, 1),
('2026-07-01 09:30:00', 6, 2),
('2026-07-01 11:00:00', 8, 3),
('2026-07-02 08:00:00', 3, 4),
('2026-07-02 09:30:00', 6, 5),
('2026-07-02 11:00:00', 8, 6),
('2026-07-03 08:00:00', 3, 7),
('2026-07-03 09:30:00', 6, 8),
('2026-07-03 11:00:00', 8, 9),
('2026-07-04 08:00:00', 3, 10),
('2026-07-04 09:30:00', 6, 1),
('2026-07-04 11:00:00', 8, 2),
('2026-07-05 08:00:00', 3, 3),
('2026-07-05 09:30:00', 6, 4),
('2026-07-05 11:00:00', 8, 5),
('2026-07-06 08:00:00', 3, 6),
('2026-07-06 09:30:00', 6, 7),
('2026-07-06 11:00:00', 8, 8),
('2026-07-07 08:00:00', 3, 9),
('2026-07-07 09:30:00', 6, 10),
('2026-07-07 11:00:00', 8, 1),
('2026-07-08 08:00:00', 3, 2),
('2026-07-08 09:30:00', 6, 3),
('2026-07-08 11:00:00', 8, 4),
('2026-07-09 08:00:00', 3, 5),
('2026-07-09 09:30:00', 6, 6),
('2026-07-09 11:00:00', 8, 7),
('2026-07-10 08:00:00', 3, 8),
('2026-07-10 09:30:00', 6, 9),
('2026-07-10 11:00:00', 8, 10);

-- Вставка данных в feedings
INSERT INTO "feedings" ("date", "animal_id", "employee_id") VALUES
('2026-07-01 07:00:00', 1, 1),
('2026-07-01 07:30:00', 2, 1),
('2026-07-01 08:00:00', 3, 4),
('2026-07-01 08:30:00', 4, 4),
('2026-07-01 09:00:00', 5, 7),
('2026-07-01 09:30:00', 6, 7),
('2026-07-02 07:00:00', 7, 1),
('2026-07-02 07:30:00', 8, 1),
('2026-07-02 08:00:00', 9, 4),
('2026-07-02 08:30:00', 10, 4),
('2026-07-02 09:00:00', 11, 7),
('2026-07-02 09:30:00', 12, 7),
('2026-07-03 07:00:00', 13, 1),
('2026-07-03 07:30:00', 14, 1),
('2026-07-03 08:00:00', 15, 4),
('2026-07-03 08:30:00', 16, 4),
('2026-07-03 09:00:00', 17, 7),
('2026-07-03 09:30:00', 18, 7),
('2026-07-04 07:00:00', 19, 1),
('2026-07-04 07:30:00', 20, 1),
('2026-07-04 08:00:00', 1, 4),
('2026-07-04 08:30:00', 2, 4),
('2026-07-05 07:00:00', 3, 7),
('2026-07-05 07:30:00', 4, 7),
('2026-07-05 08:00:00', 5, 1),
('2026-07-05 08:30:00', 6, 1),
('2026-07-06 07:00:00', 7, 4),
('2026-07-06 07:30:00', 8, 4),
('2026-07-06 08:00:00', 9, 7),
('2026-07-06 08:30:00', 10, 7),
('2026-07-07 07:00:00', 11, 1),
('2026-07-07 07:30:00', 12, 1),
('2026-07-07 08:00:00', 13, 4),
('2026-07-07 08:30:00', 14, 4),
('2026-07-08 07:00:00', 15, 7),
('2026-07-08 07:30:00', 16, 7),
('2026-07-08 08:00:00', 17, 1),
('2026-07-08 08:30:00', 18, 1),
('2026-07-09 07:00:00', 19, 4),
('2026-07-09 07:30:00', 20, 4),
('2026-07-09 08:00:00', 1, 7),
('2026-07-09 08:30:00', 2, 7),
('2026-07-10 07:00:00', 3, 1),
('2026-07-10 07:30:00', 4, 1),
('2026-07-10 08:00:00', 5, 4),
('2026-07-10 08:30:00', 6, 4),
('2026-07-10 09:00:00', 7, 7),
('2026-07-10 09:30:00', 8, 7),
('2026-07-10 10:00:00', 9, 1),
('2026-07-10 10:30:00', 10, 1);

-- Вставка данных в animal_employee_responsibles
INSERT INTO "animal_employee_responsibles" ("animal_id", "employee_id", "date") VALUES
(1, 1, '2026-07-01 06:00:00'),
(2, 1, '2026-07-01 06:00:00'),
(3, 4, '2026-07-01 06:00:00'),
(4, 4, '2026-07-01 06:00:00'),
(5, 7, '2026-07-01 06:00:00'),
(6, 7, '2026-07-01 06:00:00'),
(7, 1, '2026-07-01 06:00:00'),
(8, 1, '2026-07-01 06:00:00'),
(9, 4, '2026-07-01 06:00:00'),
(10, 4, '2026-07-01 06:00:00'),
(11, 7, '2026-07-01 06:00:00'),
(12, 7, '2026-07-01 06:00:00'),
(13, 1, '2026-07-01 06:00:00'),
(14, 1, '2026-07-01 06:00:00'),
(15, 4, '2026-07-01 06:00:00'),
(16, 4, '2026-07-01 06:00:00'),
(17, 7, '2026-07-01 06:00:00'),
(18, 7, '2026-07-01 06:00:00'),
(19, 1, '2026-07-01 06:00:00'),
(20, 1, '2026-07-01 06:00:00');

WITH  count_clianings_year AS   (
    SELECT animals.id,
        COUNT(1) cleanings_count FROM cleanings
        INNER JOIN animals ON cleanings.voliere_id = animals.voliere_id
        WHERE EXTRACT(YEAR FROM CURRENT_DATE) = EXTRACT(YEAR FROM cleanings.date) 
        GROUP BY animals.id
),
    count_feedings_year AS (
        SELECT animal_id,  COUNT(1) feedings_count FROM feedings
        WHERE EXTRACT(YEAR FROM CURRENT_DATE) = EXTRACT(YEAR FROM date) 
        GROUP BY animal_id) 
SELECT "name", cleanings_count, feedings_count FROM animals LEFT JOIN count_clianings_year  ccy ON animals.id = ccy.id 
LEFT JOIN count_feedings_year cfy ON animals.id = cfy.animal_id;



-- WITH count_by_valiere AS (
--     SELECT voliere_id, COUNT(1) AS animals_count
--     FROM animals GROUP BY voliere_id
-- ),
-- last_cleanings AS (
--     SELECT employee_id, MAX(date) AS max_date
--     FROM cleanings GROUP BY employee_id
-- )
-- SELECT c.employee_id, animals_count FROM cleanings c
--     INNER JOIN last_cleanings lc ON c.employee_id = lc.employee_id
--     INNER JOIN count_by_valiere cbv ON c.voliere_id = cbv.valiere_id
-- WHERE max_date = date;

-- SELECT name, is_watched FROM animals LEFT JOIN  (
--   SELECT f.animal_id, CURRENT_TIMESTAMP - INTERVAL '12 days' <= MAX(f.date) AS is_watched FROM feedings f 
--   INNER JOIN animal_employee_responsibles aer 
--   ON aer.employee_id = f.employee_id AND aer.animal_id = f.animal_id 
--   GROUP BY f.animal_id 
--   ) AS w ON animal_id = id
-- ;