# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

x4 = 0
y4 = 0

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
  x4 = x3
elif x1 == x3:
  x4 = x2
else:
  x4 = x1

if y1 == y2:
  y4 = y3
elif y1 == y3:
  y4 = y2
else:
  y4 = y1

print(x4, y4)