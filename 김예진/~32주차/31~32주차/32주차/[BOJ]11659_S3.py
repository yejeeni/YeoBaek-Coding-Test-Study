import sys

# 수의 개수 n, 합을 구해야하는 횟수 m
n, m = map(int, sys.stdin.readline().split())

# 숫자 n개
arr = list(map(int, sys.stdin.readline().split()))

# 누적합 방식으로 합을 미리 구해놓기
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
# print(prefix_sum)

for j in range(m):
    start, end = map(int, sys.stdin.readline().split())
    # start부터 end까지의 합 = 누적합[end] - 누적합[start-1] (-1하지 않으면 start번째 숫자도 빠짐)
    print(prefix_sum[end] - prefix_sum[start-1])