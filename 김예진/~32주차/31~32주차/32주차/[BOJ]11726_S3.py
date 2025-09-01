n = int(input())

arr = [0] * 1001 # 방법의 수를 담을 배열 초기화

arr[1] = 1
arr[2] = 2

for i in range(3, len(arr)):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n] % 10007)