import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # 2부터 √n까지 반복
        if n % i == 0:
            return False # 나눠떨어지면 소수가 아님
    return True # 끝까지 나눠떨어지지 못했으면 소수임

t = int(input())
for i in range(t):
    n = int(input())
    while True:
        if (is_prime(n)):
            print(n)
            break
        n += 1

# # 에라토스테네스의 체
# n = int(input())

# is_prime = [False, False] + [True] * (n - 1)
# # 2부터 √n까지 반복
# for i in range(2, int(n**0.5) + 1):
#     if is_prime[i]:
#         # i가 소수라면, i의 배수들은 소수가 아님

#         # i*i부터 시작하는 이유: i보다 작은 수의 배수들은 이미 이전 단계에서 지워짐
#         # 예: 2의 배수는 2단계에서, 3의 배수는 3단계에서 이미 제거됨.
#         for j in range(i * i, n + 1, i):
#             is_prime[j] = False # i의 배수를 소수가 아니라고 표시

# # 소수만 담을 리스트 생성
# primes = []
# for i in range(n + 1):
#     if is_prime[i]:
#         primes.append(i)  # True로 남아 있는 수는 소수

# for i in primes:
#     print(i)