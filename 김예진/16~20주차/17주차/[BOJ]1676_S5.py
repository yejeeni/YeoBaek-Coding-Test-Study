import math

n = int(input())

# 팩토리얼 계산해서 str로 형변환 후 뒤집음
n_factorial = str(math.factorial(n))[::-1]

count = 0
for i in n_factorial:
  if i == '0':
    count += 1
  else:
    print(count)
    break