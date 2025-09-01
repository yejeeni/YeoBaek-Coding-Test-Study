# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
# 소수: 1과 자기자신 외로는 나눠지지 않음

n = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
  is_prime = True
  # 1은 소수가 아님
  if num < 2:
    continue

  # 2부터 숫자-1까지 반복
  for i in range(2, num):
    # 숫자를 나눴을 때 나눠떨어지게 되면 소수가 아님
    if num % i == 0:
      is_prime = False
      break
      
  if is_prime:
    result += 1

print(result)