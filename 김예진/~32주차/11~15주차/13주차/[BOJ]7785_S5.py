import sys

n = int(sys.stdin.readline())
dic = {}

for i in range(n):
  name, state = map(str, sys.stdin.readline().split())

  if state == 'enter':
    dic[name] = state
  else:
    del dic[name]

arr = sorted(dic.keys(), reverse=True)
"""
키만 뽑아내기: .keys()
값만 뽑아내기: .values()
키, 값 쌍으로 뽑아내기: .items()
키를 통해서 값을 반환하기: .get()
"""

for i in arr:
  print(i)