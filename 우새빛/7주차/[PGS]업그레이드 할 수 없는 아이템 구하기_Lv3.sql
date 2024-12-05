-- 코드를 작성해주세요(실패)
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE)
ORDER BY ITEM_ID DESC
--*** 위의 코드를 사용할 시 오류 발생

""" 
[NOT IN과 NOT EXISTS]
- IN     : - 하위 쿼리의 결과값과 메인 쿼리의 값을 비교 (데이터를 비교)
           - 하위 쿼리에 NULL이 있으면 문제 발생 가능	<<<***중요
           - 작은 데이터 집합에 적합
           - 하위 쿼리 결과를 모두 가져와 비교

- EXISTS : - 하위 쿼리의 결과값이 아니라, 결과가 존재하는지 여부(TRUE/FALSE)를 판단 (존재 확인)
           - NULL 문제 없음
           - 큰 데이터 집합에 적합
           - 조건을 만족하는 첫 번째 행만 찾으면 종료
             (데이터 크기가 클수록 EXISTS를 사용하는 것이 성능 면에서 더 유리)

           - EXISTS는 데이터 존재의 여부만을 판단하므로...
             하위 쿼리에서 SELECT 1 / * / 특정쿼리 등을 사용할 수 있다
             >>> SELECT 1을 사용하면 결과가 존재하는지만 확인, 불필요한 데이터를 반환하지 않아 최적화 가능<<<
"""

-- 방법1) NOT IN을 사용하되 하위 퀴리에서 NULL이 조회 되지 않도록 하기
-- 코드를 작성해주세요
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC

--방법2) NOT EXISTS를 사용
-- 코드를 작성해주세요
SELECT INF.ITEM_ID, INF.ITEM_NAME, INF.RARITY
FROM ITEM_INFO INF JOIN ITEM_TREE TRE ON INF.ITEM_ID = TRE.ITEM_ID
WHERE NOT EXISTS (SELECT 1 FROM ITEM_TREE WHERE ITEM_TREE.PARENT_ITEM_ID = INF.ITEM_ID)
ORDER BY INF.ITEM_ID DESC