import math
left = 13
right = 17
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        y=set()
        for i in range(1, int(math.sqrt(num))+1):
              if num % i == 0:
                   y.add(i)
                   y.add(num // i) #1 13 동시저장
        if len(y) % 2 == 0:
             answer += num
        else:
             answer -= num
    return answer
solution(left, right)