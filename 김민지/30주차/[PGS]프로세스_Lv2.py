from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])  #(순서, 우선순위)
    
    while 1:
        순서, 우선순위 = queue.popleft()  #맨 앞에 꺼내기

        if any(우선순위 < q[1] for q in queue):  #any는 하나라도 참이면 참 / q[1]은 우선순위
            queue.append((순서, 우선순위))        #다시 큐에 넣기
        else:
            answer += 1                          #실행됨 -> 1 증가
            if 순서 == location:                  #우리가 찾던 프로세스라면
                return answer                    #종료