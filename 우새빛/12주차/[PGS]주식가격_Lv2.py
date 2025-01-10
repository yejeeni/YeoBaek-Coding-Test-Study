def solution(prices):
    answer = []
    
    for i in range(len(prices)): #기록된 주식
        sec = 0
        for j in range(i+1, len(prices)): #이후 주식 값 비교하여 떨어졌는지 판단
            sec += 1
            if prices[i] > prices[j]: #떨어졌다면 초 증가 그만
                break
        answer.append(sec)
        
    return answer