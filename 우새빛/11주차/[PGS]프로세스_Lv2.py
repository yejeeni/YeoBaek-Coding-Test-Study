from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    
    while location != -1:
        now = queue.popleft() #큐에서 대기 중인 큐 하나를 꺼냄
        
        check = False #대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있는지 확인
        for q in queue:
            if now < q:
                check = True
                break
        
        if check == True: #있다면 방금 꺼낸 프로세스를 다시 큐에 넣기
            queue.append(now)
            location -= 1
            if location < 0:
                location = len(queue) - 1
        else : #만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행(다시 큐에 넣지 않음)
            answer += 1
            location -= 1
            if location < 0: #이때 우리가 원하는 프로세스의 위치가 0이하라면 방금 실행됨을 의미
                location = -1
    
    return answer