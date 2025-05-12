import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
  cmd = sys.stdin.readline().split()

  if cmd[0] == 'add':
    x = int(cmd[1])
    s.add(x)

  elif cmd[0] == 'remove':
    x = int(cmd[1])
    s.discard(x)  # remove 대신 discard 쓰면 없는 값도 에러 안 남!

  elif cmd[0] == 'check':
    x = int(cmd[1])
    print(1 if x in s else 0)

  elif cmd[0] == 'toggle':
    x = int(cmd[1])
    if x in s:
      s.remove(x)
    else:
      s.add(x)

  elif cmd[0] == 'all':
    s = set(range(1, 21))

  elif cmd[0] == 'empty':
    s = set()