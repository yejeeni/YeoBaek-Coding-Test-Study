# 나이 증가 순으로, 같으면 먼저 가입한 순으로 정렬

n = int(input())
arr = []

for i in range(n):
  age, name = input().split()
  arr.append([int(age), name])

arr.sort(key= lambda x: x[0])
# 파이썬은 기본적으로 stable 정렬을 한다. 입력받은 값 중 같은 값이 있는 경우, 해당 값의 순서를 그대로 유지한다.
# 그러므로 나이 순으로 정렬하면, 중복 나이가 있을 때 자동적으로 먼저 입력받은 순으로 정렬됨

for i in arr:
  print(i[0], i[1])