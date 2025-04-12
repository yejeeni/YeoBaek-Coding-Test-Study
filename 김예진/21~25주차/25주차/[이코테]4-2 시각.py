"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중, 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
ex, N=1이면 00:00:03, 00:13:30
"""

n = int(input())

count = 0

for i in range(n+1): 
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k): # 시+분+초 문자열에 3이 포함된 경우
        count += 1

print(count)