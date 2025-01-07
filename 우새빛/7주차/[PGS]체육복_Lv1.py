def solution(n, lost, reserve):
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    
    # 여분 체육복이 있는데 도난 당한 경우 -> lost, reserve 리스트에서 제외   
    for l in list(lost): #반복문을 돌리는 리스트를 바로 돌리면 삭제되니 list로 복사하여 진행
        if l in reserve: 
                answer += 1
                lost.remove(l)
                reserve.remove(l)
    
    # 도난 당한 사람은 여분이 있는 사람이 자신의 앞뒤로 있는지 확인
    lost.sort()
    reserve.sort()
                
    for l in list(lost):
        if l - 1 in reserve:
            answer += 1
            lost.remove(l)
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            answer += 1
            lost.remove(l)
            reserve.remove(l + 1)
            
            
    return answer
