import collections

n = int(input()) # 상근이에게 주어진 숫자 카드 개수 n
n_number = list(map(int, input().split())) # 주어진 숫자 카드에 적힌 정수
m = int(input()) # 비교할 숫자 카드 개수 m
m_number = list(map(int, input().split())) # 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수

counter = collections.Counter(n_number) # 각 숫자의 개수 세기

for i in m_number:
  print(counter[i], end=' ')

# for i in m_number:
#   result.append(n_number.count(i))

# for i in result:
#   print(i, end=' ')