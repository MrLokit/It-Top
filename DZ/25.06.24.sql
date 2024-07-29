1 ---
SELECT Student.FIO
FROM Kafedra
JOIN G ON Kafedra.Kafedra = G.Kafedra
JOIN Student ON G.'Group' = Student.'Group'
WHERE Kafedra.Decanat = 'Физико-математический'
2 ---
3 ---
4 ---
5 ---
6 ---
7 ---
8 ---
9 ---
10 ---
11 ---
12 ---
13 ---
14 ---
15 ---
16 ---