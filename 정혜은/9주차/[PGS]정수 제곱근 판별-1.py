n=121
import math
def solution(n):
    answer = 0
    n_sqrt = int(math.sqrt(n))
    if (n_sqrt**2) == n:
        answer = ((n_sqrt+1)**2)
    else:
        answer = -1
    #print(answer)
    return answer
solution(n)