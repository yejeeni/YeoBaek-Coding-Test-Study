# N 킬로 설탕 배달. 봉지는 3킬로와 5킬로 봉지가 있음. 배달 최소 봉지 수는?

n = int(input())
result = 0

while n > 2:
  if n % 5 == 0: # 5로 나누어 떨어지는 경우
    n -= 5
    result += 1

  elif n % 3 == 0: # 3으로 나누어 떨어지는 경우
    n -= 3
    result += 1

  elif n > 5: # 5나 3으로 나눠 떨어지진 않지만, n이 5보다 큰 경우
    n -= 5 # result가 최소여야하므로 5를 감산
    result += 1

  elif n > 3: # 5나 3으로 나눠 떨어지진 않지만, n이 3보다 큰 경우
    n -= 3
    result += 1

if n != 0:
  print('-1')
else:
  print(result)