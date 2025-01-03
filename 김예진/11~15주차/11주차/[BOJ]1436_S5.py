# 어떤 수에 6이 적어도 3개 이상 연속으로 들어가야 한다. 666, 1666, 2666, 3666, ...
# n번째 수는 얼마인지

n = int(input())
cnt = 0
result = 666

while(True):
  if '666' in str(result):
    cnt += 1
  
  if cnt == n:
    print(result)
    break

  result += 1