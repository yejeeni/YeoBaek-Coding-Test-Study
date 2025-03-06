import sys

n = int(input())
nums = set(map(int, sys.stdin.readline().split()))
m = int(input())
cf_nums = list(map(int, sys.stdin.readline().split()))

for i in cf_nums:
  if i in nums:
    print('1', end=' ')
  else:
    print('0', end=' ')


"""
nums를 처음엔 list로 받았는데 시간초과가 발생했고, set으로 바꾸니 시간초과가 해결됨

1. 리스트에서의 탐색
if i in nums는 리스트의 첫 번째 요소부터 마지막 요소까지 하나씩 비교하여 i가 있는지 확인하므로 O(n). n은 리스트의 길이
m개의 수를 각각 리스트 nums에서 찾으려면 최악의 경우 O(m*n)

2. 집합에서의 탐색
집합은 해시 테이블 기반으로 구현되어 있어, if i in nums에서 거의 즉시 i의 존재 여부 확인 가능. O(1)
m개의 수를 각각 집합 nums에서 찾으려면 O(n)
"""