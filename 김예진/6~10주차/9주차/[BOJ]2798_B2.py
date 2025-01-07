# 숫자가 적힌 N장의 카드 중 3장을 고른다. 그 합이 M보다 크지 않은 최대값이어야 한다.

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sum = nums[i] + nums[j] + nums[k]
      if sum > result and sum <= M:
        result = sum

print(result)
