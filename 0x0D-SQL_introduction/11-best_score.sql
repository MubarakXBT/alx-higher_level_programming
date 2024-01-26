-- list all record in table second_table with score>= 10 in descending order
FROM `score_table`
SELECT `score`, `name`
WHERE `score` >= 10
ORDER BY `score` DESC;