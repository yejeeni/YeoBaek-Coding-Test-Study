def solution(n):
    answer = 0
    c = format(n, 'b').count('1')
    while 1:
        n += 1
        nxt = format(n, 'b').count('1')
        if c == nxt:
            return n
        
    return answer