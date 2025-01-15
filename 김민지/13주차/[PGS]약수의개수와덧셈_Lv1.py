import math
def divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  
                count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (divisors(i) % 2) == 0 :
            answer += i
        else:
            answer -= i
    return answer


"""
#약수의 개수가 홀수일때는 완전제곱수일때면 가능 (ex. 4-> 1,2,4  // 10 -> 1,2,5,10)
#약수는 쌍을 이루는 수가 있음을 이용
 for i in range(left,right+1):
        if int(i**0.5)==i**0.5:  #--> i^0.5이므로 i의 제곱근 
            answer -= i          # int()랑 그냥이랑 했을때 동일하면 약수의 개수는 홀수개
        else:
            answer += i
"""

