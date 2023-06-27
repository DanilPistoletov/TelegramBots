--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт июн 27 12:17:11 2023
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: phone
CREATE TABLE IF NOT EXISTS phone (number INTEGER PRIMARY KEY, namesurname TEXT, nickname TEXT, city TEXT, sex TEXT);
INSERT INTO phone (number, namesurname, nickname, city, sex) VALUES (79000000000, 'Danil Pistoletov', '0', '0', '0');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
