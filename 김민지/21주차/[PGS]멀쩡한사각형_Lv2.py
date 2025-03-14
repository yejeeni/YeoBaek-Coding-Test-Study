import math
def solution(w,h):
    #대각선을 지나는 사각형 개수 = 가로 + 세로 - 둘의 최대공약수
    answer = w * h - (w + h - math.gcd(w, h))  # gcd가 최대공약수 구하는 함수
    return answer