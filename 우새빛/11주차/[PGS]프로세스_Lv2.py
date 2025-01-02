from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    
    while location != -1:
        #대기 중인 프로세스 중 하나를 꺼냄
        now = queue.popleft()
        
        check = False
        #큐에 대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있는지 확인
        for q in queue:
            if now < q:
                check = True
                break
        
        #더 높은 프로세스가 있다면 다시 큐에 넣음
        if check == True:
            queue.append(now)
            location -= 1
            if location < 0:
                location = len(queue) - 1
        #만약 없다면 방금 꺼낸 프로세스 실행(큐에 다시 넣지 않음)
        else :
            answer += 1
            location -= 1
            if location < 0:
                location = -1 #만약 현재 위치가 0보다 작다면 방금 실행한 프로세스가 우리가 찾던 순번의 프로세스
    
    return answer