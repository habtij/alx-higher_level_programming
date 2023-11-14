-- Lists the number of records with the same score in the table
SELECT score, number FROM second_table
WHERE number = (SELECT COUNT(score) FROM second_table WHERE score = score);
