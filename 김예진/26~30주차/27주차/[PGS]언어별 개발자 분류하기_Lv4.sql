WITH FE AS(
    SELECT SUM(CODE) AS FECODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT *
FROM (
        SELECT 
        CASE
            WHEN -- A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
                (SKILL_CODE & (SELECT FECODE FROM FE)) AND (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python'))
            THEN 'A'
            WHEN -- B : C# 스킬을 가진 개발자
                SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
            THEN 'B'
            WHEN -- C : 그 외의 Front End 개발자
                SKILL_CODE & (SELECT FECODE FROM FE)
            THEN 'C'
        END AS GRADE 
        , ID
        , EMAIL
    FROM DEVELOPERS
) AS DEV -- 서브쿼리에는 alias 필수
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID ASC

/*
비트 AND 연산은 두 숫자의 같은 자리의 비트가 모두 1일 때만 1이 됨
즉, 어떤 SKILL_CODE가 특정 스킬을 가지고 있는지 확인할 때는
SKILL_CODE & 특정 CODE > 0
이렇게 하면 그 비트가 켜져 있는지 확인 가능

FE 코드는 FE 카테고리에 속한 여러 스킬들의 CODE를 다 더하여 하나의 "FE 스킬 비트 마스크" 로 쓸 수 있음
SKILL_CODE & FE 스킬 비트 마스크 > 0
이라면, FE 스킬 중 하나를 가지고 있다는 뜻
*/
