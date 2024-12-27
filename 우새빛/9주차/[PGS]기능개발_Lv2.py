from collections import deque

def solution(progresses, speeds):
    answer = []

    # 전체가 100%가 될 때까지 반복
    # 매 반복마다 진행 퍼센트를 더해가며 맨 앞의 기능이 100%가 되면 배포
    
    #앞에서부터 출력되어야함 (FIFO) -> 큐
    progress = deque(progresses)
    speed = deque(speeds)
    
    while (progress): 
        for i in range(len(progress)): #진행 상황 더하기기
            progress[i] += speed[i]
            if progress[i] > 100:
                progress[i] = 100
        
        count = 0
        while ((progress) and (progress[0] == 100)): #맨 앞이 100%가 되면 가능한 만큼 배포
            progress.popleft()
            speed.popleft()
            count += 1
        
        if count > 0:
            answer.append(count)
    
    return answer