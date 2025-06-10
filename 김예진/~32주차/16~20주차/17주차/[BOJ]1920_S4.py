# m의 숫자가 n에 있는거면 1, 아니면 0

n = int(input())
n_nums = set(map(int, input().split()))
m = int(input())
m_nums = map(int, input().split())

for i in m_nums:
  if i in n_nums:
    print('1')
  else:
    print('0')


"""
map 객체는 이터레이터라서 한 번 순회하면 내부 요소를 모두 소모해버림
여러 번 쓰려면 list() 또는 set()으로 변환하면 됨
"""