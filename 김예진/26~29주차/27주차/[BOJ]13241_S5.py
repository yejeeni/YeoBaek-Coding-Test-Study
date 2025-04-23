# 최소공배수

import math

a, b = map(int, input().split())

print(math.lcm(a, b))


# 유클리드 호제법 (https://devum.tistory.com/128)
# 최대공약수 구하기
# 2개의 자연수 a, b (a > b)에 대해서 a를 b로 나눈 나머지를 r이라 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같다

# a=72, b=30일 때, 최대공약수는 6이다.
# 30과 a를 b로 나눈 나머지인 12의 최대공약수도 6이다.
# 12와 (30%12=) 6의 최대공약수도 6이다.

# 최소공배수 L = 최대공약수 G * a * b 이다.
# a는 A를 G로 나눈 몫이다. 따라서 A 는 G * a이다.
# 마찬가지로 b = G * b 이다.

# L = G * a * b 에서 G * a = A 이기 때문에 L = A * b 와 같고,
# → G * b = B 이므로 L * G = A * (G * b) 이다
# → 따라서 L * G = A * B 이다.

# 그렇다면 최소공배수 L은 다음과 같은 식으로 구할 수 있다.
# ✔️ L = (A * B) / G

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

print(lcd(a, b))