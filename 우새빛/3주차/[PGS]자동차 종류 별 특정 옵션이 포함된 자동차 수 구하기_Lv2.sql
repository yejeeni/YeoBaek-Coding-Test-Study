-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(CAR_ID) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE('%통풍시트%') 
OR OPTIONS LIKE('%열선시트%') 
OR OPTIONS LIKE('%가죽시트%')
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC

-- '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 -> 가능한 WHERE절
-- LIKE 사용   : OPTIONS LIKE('%통풍시트%') OR ...
-- INSTR 사용  : INSTR(OPTIONS, '통풍시트') > 0 OR ...
-- REGEXP 사용 : OPTIONS REGEXP '통풍시트|열선시트|가죽시트'