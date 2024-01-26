-- LISTS ALL RECORDS OF THE TABLE `SECOND_TBALE` IN DESC ORDER
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC