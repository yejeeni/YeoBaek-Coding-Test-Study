# 심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수
# 예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다. 
# 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

import math

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

distance = []
for i in range(n-1):
    # 두 나무의 거리를 배열에 저장
    distance.append(arr[i+1] - arr[i])
    # 리스트 컴프리헨션으로 작성
    # distance = [arr[i+1] - arr[i] for i in range(n-1)]

point = math.gcd(*distance)

result = 0
for d in distance:
    result += d // point - 1 # 두 나무의 거리를 심어야하는 거리 단위로 나눔

print(result)


"""
## 리스트 컴프리헨션

result = []
for 요소 in 반복가능한_객체:
    result.append(표현식)

위 반복문을 다음과 같이 줄여 작성할 수 있다.

[표현식 for 요소 in 반복가능한_객체]

"""