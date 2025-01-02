# 정수 n이 주어졌을 때 소인수분해하는 프로그램

n = int(input())

result = []
num = 2
a = 1

while n != 1:
  if n % num == 0:
    print(num)
    a *= num
    n = n // num
  elif n % num != 0:
    num += 1