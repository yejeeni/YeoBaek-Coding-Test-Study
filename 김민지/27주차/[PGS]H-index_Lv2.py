def solution(citations):
    citations.sort(reverse=True)
    #6, 5, 3, 1, 0
    
    for i, c in enumerate(citations):
        if c < i + 1:  #c값이 i+1보다 작으면
            return i   #3인 경우 i = 3 // i가 가능한 제일 큰 수
    return len(citations)   #위에 해당되지 않으면 모든 편이 수 이상만큼 인용된것
 