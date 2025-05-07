import sys

m, n = map(int, sys.stdin.readline().split())

# 0부터 n까지 소수를 판별할 리스트 (True: 소수, False: 소수 아님)
is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, int(n**0.5) + 1):  # √n까지만 탐색
    if is_prime[i]:  # i가 소수라면
        for j in range(i * i, n + 1, i):  # i의 배수를 모두 제거
            is_prime[j] = False

# M 이상 N 이하의 소수 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)