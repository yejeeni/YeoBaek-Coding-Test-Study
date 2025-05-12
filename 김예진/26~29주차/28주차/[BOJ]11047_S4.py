"""
n종류의 동전을 사용하여 가치의 합을 k로 만들기 위해 필요한 동전 개수의 최솟값
"""

n, k = map(int, input().split())

coins = []
for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True) # 가치가 높은 순으로 정렬

result = 0
for coin in coins:
  if k >= coin: # k가 동전보다 값이 큰 경우, 그 동전으로 k를 나눌 수 있음
    result += k // coin # k를 coin으로 나눈 몫을 result에 더함
    k %= coin # k는 나머지로 갱신
    if k == 0: # k가 0이면 계산이 끝났으므로 break
      break

print(result)