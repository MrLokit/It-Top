1 --- SELECT * FROM '18.06.24' WHERE ID_salespeople IS NULL
2 --- SELECT Rem, Id, Country FROM '18.06.24' WHERE Country = 'Беларусь'
3 --- DELETE FROM '18.06.24' WHERE Country = 'Германия'
4 --- UPDATE '18.06.24' SET Country = 'Россия' WHERE Country = 'Польша'
5 --- -------------
6 --- SELECT Produce, Price, ID FROM '18.06.24' WHERE Color <> 'ч'
7 --- INSERT INTO '18.06.24' (ID, Produce, Material, Color, Size, Country, ID_salespeople, Rem) VALUES (1046, 'NTC-117BK', 'нейлон', 'ч', '13,3x8,3x5,7', 'Беларусь', 2016, 'Micro Camera Case')
8 --- INSERT INTO '18.06.24' (Produce, Material, Color, Size, Rem) VALUES ('POC-463BK', 'полиэстер', 'ч', '11x7x4,5', 'Compact Camera Case')
9 --- SELECT ID, Produce, Rem FROM '18.06.24' WHERE ID_salespeople = 2065 AND Country = 'Россия'
10 --- SELECT ID, Produce, Rem, Price FROM '18.06.24' WHERE Price >= 200 AND Price <= 345
11 --- SELECT ID, Produce, Material, Size FROM '18.06.24' WHERE Produce = 'сумка' AND Material = 'кожа' AND Size LIKE '40%x30%x5%'
12 --- SELECT ID, Produce, ID_salespeople, Price, Count FROM '18.06.24' WHERE Price * Count < 1200
13 --- UPDATE '18.06.24' SET ID_salespeople = 2000 WHERE Price * Count < 500
14 --- SELECT ID, Produce, Material, Count, Price FROM '18.06.24' WHERE Produce = 'сумка' AND Material = 'кожа' AND Count < 5 AND Count * Price <= 450
15 --- SELECT ID, Produce, Material, Price FROM '18.06.24' WHERE Produce = 'сумка' AND Material = 'нейлон' AND Price <= 250
16 --- UPDATE '18.06.24' SET Material = 'брезент' WHERE Produce = 'сумка' AND Price < 200
17 --- SELECT ID, Produce, Rem FROM '18.06.24' WHERE Produce = 'сумка' AND Rem = 'косметичка'
18 --- SELECT ID, Produce, Material, Color, Country FROM '18.06.24' WHERE Produce = 'сумка' AND Material = 'кожа' AND Color = 'ч' AND Country = 'Китай'
19 --- SELECT ID, Produce, Size, Rem FROM "18.06.24" WHERE Produce = 'сумка' AND CAST(substr(Rem, instr(Rem, '(') + 1, instr(Rem, ')') - instr(Rem, '(') - 1) AS INTEGER) > 15
20 --- SELECT ID, Produce, ID_salespeople, Color FROM "18.06.24" WHERE Produce = 'сумка' AND Color <> 'ч'
21 --- UPDATE '18.06.24' SET Material = 'нейлон' WHERE Produce = 'сумка' AND Material = 'полиэстер' AND Country = 'Китай'
22 --- UPDATE '18.06.24' SET Material = 'полиэстер' WHERE ID IN (1015, 1041, 1032, 1010) AND Material = 'нейлон' AND Country = 'Китай'