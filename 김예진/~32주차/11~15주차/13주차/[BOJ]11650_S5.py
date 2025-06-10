n = int(input())
arr = []
for i in range(n):
  x, y = map(int, input().split())
  arr.append([x, y]) # 2차원 배열로 추가

arr.sort() 
# 만약 두번째 값을 기준으로 내림차순하는 경우, sort 함수 인자로 key = function을 넣으면 됨
# 예를 들어 두 번째 값을 기준으로 오름차순으로 정렬을 하는데 두 번째 값이 같을 때에는 첫 번째 값을 기준으로 오름차순으로 하고싶다면
# li.sort(key = lambda x: (x[1], x[0]))

for i in arr:
  print(i[0], i[1])