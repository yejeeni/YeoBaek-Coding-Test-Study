n = int(input())

stairs = [0] * 301 # 계단 점수 배열

# 계단 점수 입력 받음
for i in range(1, n+1):
    stairs[i] = int(input())

# dp 배열 초기화
dp = [0] * 301 # 인덱스번째까지의 점수 최댓값을 저장할 배열
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2] # 고정된 값들 계산

for i in range(3, n+1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])

print(dp[n])