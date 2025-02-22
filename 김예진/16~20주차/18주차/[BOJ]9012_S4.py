"""
(), (x), (())(): VPS
(()(, (()): VPS 아님
모든 괄호를 확인하고, 스택이 비어있는지 확인
"""

t = int(input())

for i in range(t):
  left = []
  arr = list(input())

  for ch in arr:
    if ch == '(':
      left.append(ch)

    elif ch == ')':
      if not left:
        print('NO')
        break
      else:
        left.pop()
  else: # for문이 정상 종료되었을 때 실행
    if not left:
      print('YES')
    else:
      print('NO')