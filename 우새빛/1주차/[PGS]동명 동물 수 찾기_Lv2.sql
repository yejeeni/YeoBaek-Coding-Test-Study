-- 코드를 입력하세요
SELECT NAME, count(*) as COUNT FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME 
HAVING count(*) >= 2
ORDER BY NAME