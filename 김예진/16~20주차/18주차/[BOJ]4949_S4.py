"""
왼쪽 괄호를 저장해놓고, 오른쪽 괄호가 나오면 최근에 저장한 왼쪽 괄호와 비교
1. 짝이 맞으면 OK
2. 짝이 맞지 않으면 균형 깨짐
3. 오른쪽 괄호가 나왔는데, 왼쪽 괄호가 남아있지 않으면 균형 깨짐
4. 왼쪽 괄호가 남아있는데, 모든 문자열을 봤으면 균형 깨짐
-> 왼쪽 괄호가 나오면 스택에 저장해놓고 꺼내는 LIFO
"""

while True:
  brackets = []
  result = 'yes'

  arr = input()
  if arr == '.':
    break

  for ch in arr:
    if ch in ['(', '[']: # 왼쪽 괄호인 경우
      brackets.append(ch) # 리스트에 추가

    elif ch in  [')', ']']: # 오른쪽 괄호인 경우
      if not brackets: # 스택이 비어있다면 균형 깨짐
        result = 'no'
        break

      last_bracket = brackets.pop() # 마지막으로 저장한 왼쪽 괄호
      if (last_bracket == '(' and ch == ')') or (last_bracket == '[' and ch == ']'): # 짝이 맞다면 continue
        continue
      else: # 짝이 안 맞다면 균형 깨짐
        result = 'no'
        break

  if brackets: # 스택에 남은 괄호가 있다면 균형 깨짐
    result = 'no'

  print(result)