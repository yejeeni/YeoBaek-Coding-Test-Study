"""
i = 1, 2 ... 에 대해 규칙에 따라 문자열을 출력
i = 3의 배수이자 5의 배수: FizzBuzz
i = 3의 배수이지만 5의 배수가 아님: Fizz
i = 3의 배수는 아니지만 5의 배수: Buzz
i = 3의 배수도 5의 배수도 아님: i
"""

arr = []
for i in range(3):
  arr.append(input())

for idx, value in enumerate(arr):
  # 문자열 3개 중 숫자를 찾음
  if value.isdigit():
    num = (int(value) + 3 - idx)

if num % 3 == 0 and num % 5 == 0:
  print("FizzBuzz")
elif num % 3 == 0:
  print("Fizz")
elif num % 5 == 0:
  print("Buzz")
else:
  print(num)