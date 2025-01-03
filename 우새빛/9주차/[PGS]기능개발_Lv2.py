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
            if progress[i] > 100: progress[i] = 100
        
        count = 0
        while ((progress) and (progress[0] == 100)): #맨 앞이 100%가 되면 가능한 만큼 배포
            progress.popleft()
            speed.popleft()
            count += 1
        
        if count > 0:
            answer.append(count)
    
    return answer

"""
위의 코드에서 굳이 progress와 speeds를 deque()하지 않고 pop할 때 pop(0)을 사용하면
리스트 형식에서 바로 FIFO 가능 (리스트를 큐처럼 사용 가능)
그러나, pop(0)을 사용하면 리스트의 모든 요소를 한 칸씩 앞으로 밀어야 하므로, 시간 복잡도가 O(n)
        popleft()는 성능 O(1)
따라서 deque()의 성능(O(n))을 고려하여도 결과적으로는 deque를 사용하는게 성능에는 더 좋을 수 있다.
"""