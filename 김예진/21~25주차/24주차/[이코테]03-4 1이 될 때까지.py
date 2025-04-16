"""
N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행한다. 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능하다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
수행횟수의 최솟값은?
"""

n, k = map(int, input().split())
count = 0

while n != 1:
  if n % k == 0:
    n = n // k
  else:
    n -= 1
  count += 1

print(count)


# 최적화
# n이 k로 나누어 떨어지지 않는 경우, n을 1씩 빼는 대신 한 번에 k로 나누어 떨어지는 수로 만들기
n, k = map(int, input().split())
count = 0

while True:
  # N이 K로 나누어떨어지는 수가 될 때까지 1씩 뺀다
  target = (n // k) * k
  count += n - target # 1씩 빼는 연산을 하는 횟수
  n = target

  # 더이상 나눌 수 없으면 종료
  if n < k:
    break
  else:
    n = n // k
    count += 1

count += n - 1

print(count)