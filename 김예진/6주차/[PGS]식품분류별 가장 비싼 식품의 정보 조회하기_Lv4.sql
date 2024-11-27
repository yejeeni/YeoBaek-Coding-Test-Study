-- GROUP BY는 원하는 집계 결과를 얻기 위한 도구이고, 그룹화되지 않은 컬럼은 집계 이후 조인이나 서브쿼리를 통해 찾아야 한다.

WITH TEMP_TABLE AS (
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
    -- 그룹화되지 않은 컬럼은 GROUP BY와 함께 사용할 경우 명확히 어떤 값을 선택해야 하는지 알 수 없음
    -- 그러므로 여기선 CATEGORY 별 MAX_PRICE를 검색
)

SELECT FP.CATEGORY, TEMP.MAX_PRICE, FP.PRODUCT_NAME
FROM FOOD_PRODUCT FP
JOIN TEMP_TABLE TEMP
    ON FP.CATEGORY = TEMP.CATEGORY AND FP.PRICE = TEMP.MAX_PRICE
    -- FP와 조인을 통해 해당 CATEGORY와 PRICE가 일치하는 데이터를 검색
ORDER BY TEMP.MAX_PRICE DESC