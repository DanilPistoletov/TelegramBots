--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 27 12:15:11 2023
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: phone
CREATE TABLE IF NOT EXISTS phone (number INTEGER PRIMARY KEY, namesurname TEXT, nickname TEXT, city TEXT, sex TEXT);
INSERT INTO phone (number, namesurname, nickname, city, sex) VALUES (79000000000, '����� ����������', '0', '0', '0');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
