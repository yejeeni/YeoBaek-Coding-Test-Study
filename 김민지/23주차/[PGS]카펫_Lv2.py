def solution(brown, yellow):
    answer = []
    면적 = brown + yellow
    테두리 = brown
    for x in range(면적, 1, -1):
        y = 면적 // x
        if x * y != 면적:
            continue
        if x + y - 2 == brown/2:
            answer.append(x)
            answer.append(y)
            break
    
    return answer

# 2x + 2y - 4 = brown
# x + y = brown/2 + 2
# x * y = brown + yellow