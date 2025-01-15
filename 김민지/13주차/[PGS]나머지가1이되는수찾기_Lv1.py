def solution(n):
    answer = 0
    i = 1
    while 1:
        if n % i == 1:
            answer = i
            break
        i += 1
            
    return answer