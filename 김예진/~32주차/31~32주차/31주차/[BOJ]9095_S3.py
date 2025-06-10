"""
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
"""

arr = [0] * 12

arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 12):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(arr[n])