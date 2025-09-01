"""
pypy3로 제출하면 성공이긴 한데, python3으로 푸는 방법도 생각해봐야될 것 같음
"""

import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):    
    minimum = sys.maxsize # 정수 자료형의 최대값
    for j in range(1, int(i**0.5 + 1)): # 제곱근까지만
        minimum = min(minimum, dp[i-(j**2)])
    dp[i] = minimum + 1

print(dp[n])