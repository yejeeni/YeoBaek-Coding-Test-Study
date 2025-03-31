"""
1. 숫자 카드들이 N * M 형태로 놓여 있다.
2. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 3번에서 뽑힌 카드의 숫자가 가장 높기 위해선 어떤 카드를 선택해야 하는지 출력 
"""

n, m = map(int, input().split())

result = 0
for i in range(n):
  arr = list(map(int, input().split()))
  min_value = min(arr) # 각 행에서 가장 작은 값
  result = max(result, min_value) # 현재까지의 최소값 중 가장 큰 값

print(result)