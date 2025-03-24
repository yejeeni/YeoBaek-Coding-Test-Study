"""
입력: 4, 3, 6, 8, 7, 5, 2, 1
1, 2, 3, 4      + + + +
1, 2            - -         4, 3
1, 2, 5, 6      + +     
1, 2, 5         -           6
1, 2, 5, 7, 8   + +       
x               - - - - -   8, 7, 5, 2, 1
                            -> 4, 3, 6, 8, 7, 5, 2, 1
"""
stack = []
result = []
count = 1
is_able = True

n = int(input())

for i in range(n):
  num = int(input())

  while (count <= num):
    stack.append(count)
    result.append('+')
    count += 1

  if stack[-1] == num:
    stack.pop()
    result.append('-')
  else:
    is_able = False

if not is_able:
  print('NO')
else:
  for i in result:
    print(i)