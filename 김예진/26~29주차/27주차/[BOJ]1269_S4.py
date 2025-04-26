# 대칭 차집합: 두 집합 A, B가 있을 때, (A-B)와 (B-A)의 합집합

a, b = map(int, input().split())

# 집합 A
a_set = set(map(int, input().split()))
# 집합 B
b_set = set(map(int, input().split()))

result = (a_set - b_set) | (b_set - a_set)

print(len(result))