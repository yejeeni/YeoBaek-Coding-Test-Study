# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
# N은 1 이상 10,000 이하이다. K는 1 이상 N 이하

n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
  if n % i == 0:
    cnt += 1
    if cnt == k:
      print(i)

if cnt < k:
  print(0)