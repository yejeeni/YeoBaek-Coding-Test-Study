SELECT 
    ID
    , CASE
        -- NTILE(): PARTITION을 지정된 수 만큼의 등급으로 나누어 각 등급 번호를 출력
        -- SELECT NTILE([나눌 그룹의 정수]) OVER (PARTITION BY [col1] ORDER BY [col2])
        -- PARTITION BY를 생략하면 전체 행(N)에 대해 그룹화하고, 지정하면 해당 파티션(컬럼) 내에서 그룹화
        -- ORDER BY는 PARTITION에 지정된 컬럼에 대해 정렬
        WHEN NTILE(4) OVER(ORDER BY SIZE_OF_COLONY) = 1 THEN 'LOW'
        WHEN NTILE(4) OVER(ORDER BY SIZE_OF_COLONY) = 2 THEN 'MEDIUM'
        WHEN NTILE(4) OVER(ORDER BY SIZE_OF_COLONY) = 3 THEN 'HIGH'
        ELSE 'CRITICAL'
    END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID ASC