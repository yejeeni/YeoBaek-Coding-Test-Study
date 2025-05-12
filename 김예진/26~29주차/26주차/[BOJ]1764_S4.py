n, m = map(int, input().split())

n_people = set()
for i in range(n):
  n_people.add(input())

m_people = set()
for i in range(m):
  m_people.add(input())

# set은 집합 데이터형이므로 집합 연산을 사용할 수 있다.
result = sorted(n_people & m_people)

print(len(result))
for i in result:
  print(i)

# people = []
# result = []

# for i in range(n):
#   people.append(input())

# for i in range(m):
#   now = input()
#   if now in people:
#     result.append(now)
#   else:
#     continue

# print(len(result))
# for i in result:
#   print(i)