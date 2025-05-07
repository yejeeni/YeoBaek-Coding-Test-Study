import math
from functools import reduce

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    return reduce(lcm, arr)


#reduce는 functools 모듈에 포함된 함수로, 리스트나 튜플 같은 반복 가능한 객체의 요소들을 누적하여 하나의 값으로 줄이는 역할을 합니다.