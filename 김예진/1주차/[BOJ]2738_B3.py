# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

n, m = map(int, input().split())
A, B = [], []

for i in range(n):
  a = list(map(int, input().split()))
  A.append(a)

for i in range(n):
  b = list(map(int, input().split()))
  B.append(b)

for i in range(n):
  for j in range(m):
    print(A[i][j] + B[i][j], end=' ')
  print()