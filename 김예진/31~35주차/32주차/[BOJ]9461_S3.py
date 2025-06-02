p = [0] * 101

p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for i in range(6, 101):
  # 점화식: P(n) = P(n-1) + P(n-5)
  p[i] = p[i-5] + p[i-1] 

t = int(input())

for i in range(t):
  n = int(input())
  print(p[n])