import sys
from collections import Counter

n = int(sys.stdin.readline()) # n은 홀수
arr = []
for _ in range(n):
  arr.append(int(sys.stdin.readline()))

# 평균
print(round(sum(arr) / n))

# 중앙값
arr.sort()
print(arr[n // 2])

# 최빈값
counter = Counter(arr)
most_common = counter.most_common() # counter의 상위 요소 반환
max_frequency = most_common[0][1] # 가장 높은 빈도수
modes = [] # 최빈값을 저장할 리스트

for num, count in most_common:
  if count == max_frequency:
    modes.append(num)

if len(modes) > 1: # 최빈값이 하나 이상인 경우
  modes.sort()
  mode = modes[1] # 두 번째로 작은 값
else:
  mode = modes[0]
print(mode)

# 범위
print(arr[-1] - arr[0])