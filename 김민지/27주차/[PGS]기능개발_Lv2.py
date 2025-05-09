def solution(progresses, speeds):
    answer = []
    
    while progresses:
        # 하루 진도 증가
        progresses = [p + s for p, s in zip(progresses, speeds)]
        
        count = 0
        # 앞에서부터 100 이상인 기능 세기
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        if count > 0:
            answer.append(count)
    
    return answer