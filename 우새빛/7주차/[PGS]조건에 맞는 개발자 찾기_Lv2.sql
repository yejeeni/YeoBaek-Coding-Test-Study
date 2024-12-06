-- 코드를 작성해주세요
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) > 0 
                                    -- AND 연산을 통해서 포함하는지 확인
WHERE S.NAME IN ('Python', 'C#')
ORDER BY D.ID ASC