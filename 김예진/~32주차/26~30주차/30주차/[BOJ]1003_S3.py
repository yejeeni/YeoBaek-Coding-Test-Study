f0 = [1, 0]
f1 = [0, 1]

for i in range(2, 41):
  f0.append(f0[i-1] + f0[i-2])
  f1.append(f1[i-1] + f1[i-2])

t = int(input())
for i in range(t):
  n = int(input())
  print(f0[n], f1[n])