def solution(sizes):
    answer = 0
    h = 0
    w = 0
    
    for size in sizes:
        size.sort()  #앞에 작은거 뒤어 큰거

        if h < size[0]:
            h = size[0]
        if w < size[1]:
            w = size[1]
        
    answer = h*w
    return answer