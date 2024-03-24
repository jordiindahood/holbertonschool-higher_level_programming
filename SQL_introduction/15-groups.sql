-- script 15
SELECT
	score,
	count(*) as number
FROM
	second_table
GROUP BY
	score
ORDER BY
	number DESC;