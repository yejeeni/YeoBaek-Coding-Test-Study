import math
def divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    n_list = []
    for n in range(1, number+1):
        a = divisors(n)
        if a > limit:
            a = power
        n_list.append(a)
    
    answer = sum(n_list)
    
    return answer