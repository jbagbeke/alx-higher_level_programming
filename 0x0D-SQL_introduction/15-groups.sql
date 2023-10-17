--Group/sort by score

SELECT score, COUNT(*) as number
FROM hbtn_0c_0.second_table GROUP BY score
ORDER BY number DESC;
