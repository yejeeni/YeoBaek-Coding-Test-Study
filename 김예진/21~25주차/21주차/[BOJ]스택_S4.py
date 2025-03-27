import sys

# 시간초과 -> input 대신 sys.stdin.readline.strip()
n = int(sys.stdin.readline().strip())

stack = []

for i in range(n):
  cmd = sys.stdin.readline().strip().split()

  if cmd[0] == 'push':
    stack.append(cmd[1])
  
  elif cmd[0] == 'pop':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  
  elif cmd[0] == 'size':
    print(len(stack))
  
  elif cmd[0] == 'empty':
    if len(stack) < 1:
      print(1)
    else:
      print(0)
  
  elif cmd[0] == 'top':
    if len(stack) > 0:
      print(stack[-1])
    else:
      print(-1)