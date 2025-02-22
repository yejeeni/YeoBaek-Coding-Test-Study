# m개의 문자열 중에 총 몇개가 n개의 단어로 된 집합 s에 포함되는지

n, m = map(int, input().split())

s = set()
for i in range(n):
  s.add(input())

result = 0
for i in range(m):
  if input() in s:
    result += 1

print(result)

# 처음엔 리스트로 풀어서 정답을 맞추긴 했으나, 시간이 오래걸리는 것 같아 list를 set으로 바꿈
# 집합 두 개를 만들어둔 것을 반복문에서 입력을 바로 탐색하는 것으로 개선