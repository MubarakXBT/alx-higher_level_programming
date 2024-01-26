-- list all record in table second_table with score>= 10 in descending order
SELECT `score`, `name`
FROM `score_table`
WHERE `score` >= 10
ORDER BY `score` DESC;