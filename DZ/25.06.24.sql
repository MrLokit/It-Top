1 ---
SELECT S.FIO
FROM Student S
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE K.Decanat = 'Физико-математический'
2 ---
SELECT G.Kafedra, K.Decanat
FROM Student S
JOIN Exzamen E ON S.ID_St = E.Id_St
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE E.Predmet = 'Социология'
3 ---
SELECT K.Kafedra, S.FIO
FROM Kafedra K
JOIN G ON K.Kafedra = G.Kafedra
JOIN Student S ON G.[Group] = S.[Group]
ORDER BY S.FIO
4 ---
SELECT Z.N_Z
FROM Student S
JOIN Zachetki Z ON S.ID_St = Z.Id_Studenta
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE K.Decanat = 'Физико-технический'
5 ---
SELECT S.FIO
FROM Student S
JOIN Exzamen E ON S.ID_St = E.Id_St
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE K.Decanat = 'Физико-технический' AND E.Predmet = 'Иностр. язык' AND E.Ball = 5
6 ---
SELECT COUNT(DISTINCT Predmet) AS TotalSubjects FROM Exzamen
7 ---
SELECT AVG(Ball) AS AverageScore
FROM Exzamen
WHERE Id_St IN (SELECT ID_St FROM Student WHERE FIO LIKE '%Васильева%')
8 ---
SELECT Special, COUNT(ID_St) AS TotalStudents
FROM Student
GROUP BY Special
9 ---
SELECT [Group]
FROM G
WHERE Kafedra = 'Каф. Технологии'
10 ---
SELECT S.FIO
FROM Student S
JOIN Exzamen E ON S.ID_St = E.Id_St
WHERE E.Predmet = 'Дифференциальные уравнения' AND E.Ball = 5
11 ---
SELECT COUNT(*) AS TotalExams
FROM Exzamen
WHERE Id_St = (SELECT ID_St FROM Student WHERE FIO LIKE '%Шутов%')
12 ---
SELECT DISTINCT K.Kafedra
FROM Kafedra K
LEFT JOIN G ON K.Kafedra = G.Kafedra
LEFT JOIN Exzamen E ON G.[Group] = E.Id_St
WHERE E.Id_St IS NULL
13 ---
SELECT Kafedra, COUNT(*) AS TotalDepartments
FROM Kafedra
GROUP BY Decanat
14 ---
SELECT COUNT(*) AS TotalAPluses
FROM Exzamen E
JOIN Student S ON E.Id_St = S.ID_St
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE K.Decanat = 'Физико-математический' AND E.Ball = 5
15 ---
SELECT Z.N_Z
FROM Zachetki Z
JOIN Student S ON Z.Id_Studenta = S.ID_St
JOIN G ON S.[Group] = G.[Group]
WHERE G.[Group] = 'ФТ151'
16 ---
SELECT DISTINCT Special
FROM Student S
JOIN G ON S.[Group] = G.[Group]
JOIN Kafedra K ON G.Kafedra = K.Kafedra
WHERE K.Decanat = 'Физико-математический'