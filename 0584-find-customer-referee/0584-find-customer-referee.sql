# Write your MySQL query statement below
SELECT name from Customer
Where id not in (select id from Customer where referee_id = '2')