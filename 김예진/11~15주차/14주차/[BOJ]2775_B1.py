# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 
# k층의 n호에는 몇 명이 사는지. 1 ≤ k, n ≤ 14


t = int(input())

for _ in range(t):
  k = int(input())
  n = int(input())
  # k층의 n호에는 k-1층의 1호부터 n호까지 사람들의 수의 합만큼 생활
  
  arr = [i for i in range(1, n+1)] # 0층 n호실까지 사람들의 수
  
  for i in range(k):
    for j in range(1, n): # arr[0]은 1명 고정이라 arr[1]부터
      arr[j] += arr[j-1] 

  print(arr[-1])