# 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값

n = int(input()) # 사람 수
p = list(map(int, input().split())) # 수행시간
p.sort()

result = 0
for i in range(1, n+1):
    result += p[n-i] * (i)
print(result)