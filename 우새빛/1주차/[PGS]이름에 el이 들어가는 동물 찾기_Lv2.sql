-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%'
                              -- 대소문자 구분시 BINARY NAME LIKE '%el%'
ORDER BY NAME