# round 함수는 사사오입의 원칙을 따른다. 5에서 반올림 할때, 앞자리 숫자가 홀수면 올림, 짝수면 내림을 한다

import sys

def my_round(n):
  if n - int(n) >= 0.5:
    return int(n) + 1
  else:
    return int(n)

n = int(sys.stdin.readline().strip())

if n == 0:
  print(0)
else:
  comments = []
  for _ in range(n):
    comments.append(int(sys.stdin.readline().strip()))
  comments.sort()
  
  cut_line = my_round(n * 0.15)

  print(my_round((sum(comments[cut_line:n-cut_line]) / (len(comments[cut_line:n-cut_line])))))