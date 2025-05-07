def solution(elements):
    answer = 0
    
    n = len(elements)
    elements = elements * 2 #순환을 위해 2번 반복
    
    sum_set = set() #합을 넣을 set(중복 방지)
    
    for i in range(1, n+1): #길이
        for j in range(n): #시작점
            sum_set.add(sum(elements[j:j+i]))
    
    answer = len(sum_set) #합을 담은 set의 길이 = 가지 수
    
    return answer