-- 코드를 작성해주세요
SELECT COUNT(*) as FISH_COUNT
FROM FISH_INFO
WHERE LENGTH IS NULL

""" 
조건) 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 NULL 이며...
문제) 잡은 물고기 중 길이가 10cm 이하인 물고기의 수를 출력하는 SQL 문을 작성해주세요.
-> 길이가 NULL인 행을 찾으면 됨
"""