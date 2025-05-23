/*
자동차 정보 CAR_RENTAL_COMPANY_CAR 
대여 기록 정보 CAR_RENTAL_COMPANY_RENTAL_HISTORY
종류,기간 별 할인 정책 CAR_RENTAL_COMPANY_DISCOUNT_PLAN
*/

-- 세단 or SUV 중, 2022년 11월 1일부터 2022년 11월 30일까지 대여 중인 자동차 (제외해야 하는 대상)
WITH RENTALING AS (
    SELECT CAR.CAR_ID
    FROM CAR_RENTAL_COMPANY_CAR CAR
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY HISTORY
        ON CAR.CAR_ID = HISTORY.CAR_ID
    WHERE CAR.CAR_TYPE IN ('세단', 'SUV')
        AND (END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30')
    GROUP BY CAR.CAR_ID
),
     
-- 할인이 적용된 대여 금액
DAYS_30_FEE AS (
    SELECT CAR_ID
        , CAR.CAR_TYPE
        , CAR.DAILY_FEE * 30 * (1 - PLAN.DISCOUNT_RATE / 100) AS FEE
    FROM CAR_RENTAL_COMPANY_CAR CAR
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN PLAN
        ON CAR.CAR_TYPE = PLAN.CAR_TYPE
    WHERE DURATION_TYPE = "30일 이상"
)

SELECT CAR.CAR_ID
    , CAR.CAR_TYPE
    , TRUNCATE(FEE30.FEE, 0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CAR
JOIN DAYS_30_FEE FEE30
    ON CAR.CAR_ID = FEE30.CAR_ID
WHERE CAR.CAR_TYPE IN ('세단', 'SUV')
    AND CAR.CAR_ID NOT IN (SELECT * FROM RENTALING)
    # 50만원 이상 200만원 미만
    AND FEE30.FEE >= 500000 AND FEE30.FEE < 2000000
ORDER BY FEE DESC, CAR.CAR_TYPE ASC, CAR.CAR_ID DESC