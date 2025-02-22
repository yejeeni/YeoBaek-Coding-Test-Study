import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
  arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(n):
  print(arr[i])

# N(1 ≤ N ≤ 1,000,000)이라 입출력 방식이 느려 input을 사용하면 시간 초과가 난다. 
# 이런 경우 input 대신 sys.stdin.readline을 사용할 수 있다. 문자열을 저장하고 싶은 경우 .rstrip() 추가.
# 참고 - https://www.acmicpc.net/problem/15552