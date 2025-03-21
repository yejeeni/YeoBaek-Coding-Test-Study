import math
def solution(r1, r2):
    answer = 0  
    num = 0
    for i in range(1, r2+1):
        NumInR2 = int(math.sqrt(r2**2-i**2))  #소수점 버림
        NumInR1 = math.ceil(math.sqrt(r1**2-i**2)) if r1 > i else 0 # 소수점 올림
        num += NumInR2 - NumInR1 + 1  #큰원의 낮은 정수 - 작은원의 높은 정수 +1 = i의 점 개수
    answer = num * 4

    return answer

# 시간복잡도 O(r2)