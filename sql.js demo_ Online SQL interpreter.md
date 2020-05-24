sql.js demo: Online SQL interpreter

 [![68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f6c6566745f7265645f6161303030302e706e67](../_resources/f9c82f590c4e69f53f8936be18fd4c06.png)](https://github.com/kripken/sql.js)

# Online SQL interpreter

   Enter some SQL

xxxxxxxxxx

1
DROP  TABLE  IF  EXISTS employees;
2
CREATE  TABLE employees( id integer, name text,
3
designation text, manager integer,
4
hired_on date, salary integer,
5
commission float, dept integer);
6
​
7

 INSERT  INTO employees VALUES  (1,'JOHNSON','ADMIN',6,'1990-12-17',18000,NULL,4);

8

 INSERT  INTO employees VALUES  (2,'HARDING','MANAGER',9,'1998-02-02',52000,300,3);

9

 INSERT  INTO employees VALUES  (3,'TAFT','SALES I',2,'1996-01-02',25000,500,3);

10

 INSERT  INTO employees VALUES  (4,'HOOVER','SALES I',2,'1990-04-02',27000,NULL,3);

11

 INSERT  INTO employees VALUES  (5,'LINCOLN','TECH',6,'1994-06-23',22500,1400,4);

12

 INSERT  INTO employees VALUES  (6,'GARFIELD','MANAGER',9,'1993-05-01',54000,NULL,4);

13
 INSERT  INTO employees VALUES  (7,'POLK','TECH',6,'1997-09-22',25000,NULL,4);
14

 INSERT  INTO employees VALUES  (8,'GRANT','ENGINEER',10,'1997-03-30',32000,NULL,2);

15

 INSERT  INTO employees VALUES  (9,'JACKSON','CEO',NULL,'1990-01-01',75000,NULL,4);

16

 INSERT  INTO employees VALUES  (10,'FILLMORE','MANAGER',9,'1994-08-09',56000,NULL,2);

17

 INSERT  INTO employees VALUES  (11,'ADAMS','ENGINEER',10,'1996-03-15',34000,NULL,2);

18

 INSERT  INTO employees VALUES  (12,'WASHINGTON','ADMIN',6,'1998-04-16',18000,NULL,4);

19

 INSERT  INTO employees VALUES  (13,'MONROE','ENGINEER',10,'2000-12-03',30000,NULL,2);

20

 INSERT  INTO employees VALUES  (14,'ROOSEVELT','CPA',9,'1995-10-12',35000,NULL,1);

21
​
22

SELECT designation,COUNT(*)  AS nbr,  (AVG(salary))  AS avg_salary FROM employees GROUP  BY designation ORDER  BY avg_salary DESC;

23
SELECT name,hired_on FROM employees ORDER  BY hired_on;

 Load an SQLite database file:

| designation | nbr | avg_salary |
| --- | --- | --- |
| CEO | 1   | 75000 |
| MANAGER | 3   | 54000 |
| CPA | 1   | 35000 |
| ENGINEER | 3   | 32000 |
| SALES I | 2   | 26000 |
| TECH | 2   | 23750 |
| ADMIN | 2   | 18000 |

| name | hired_on |
| --- | --- |
| JACKSON | 1990-01-01 |
| HOOVER | 1990-04-02 |
| JOHNSON | 1990-12-17 |
| GARFIELD | 1993-05-01 |
| LINCOLN | 1994-06-23 |
| FILLMORE | 1994-08-09 |
| ROOSEVELT | 1995-10-12 |
| TAFT | 1996-01-02 |
| ADAMS | 1996-03-15 |
| GRANT | 1997-03-30 |
| POLK | 1997-09-22 |
| HARDING | 1998-02-02 |
| WASHINGTON | 1998-04-16 |
| MONROE | 2000-12-03 |

Original work by kripken ([sql.js](https://github.com/kripken/sql.js)). C to Javascript compiler by kripken ([emscripten](https://github.com/kripken/emscripten)). Project now maintained by [lovasoa](https://github.com/lovasoa)