from collections import deque
import sys

n = int(sys.stdin.readline().strip())
queue = deque()

for i in range(n):
  cmd = sys.stdin.readline().strip().split() # 단어 단위로 명령을 받음

  if cmd[0] == 'push':
    queue.append(cmd[1])

  elif cmd[0] == 'pop':
    if len(queue) != 0:
      print(queue.popleft())
    else:
      print(-1)
  
  elif cmd[0] == 'size':
    print(len(queue))
  
  elif cmd[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  
  elif cmd[0] == 'front':
    if len(queue) != 0:
      print(queue[0])
    else:
      print(-1)

  elif cmd[0] == 'back':
    if len(queue) != 0:
      print(queue[-1])
    else:
      print(-1)