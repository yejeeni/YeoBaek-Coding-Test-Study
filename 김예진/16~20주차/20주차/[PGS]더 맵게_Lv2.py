# 배열로 했더니 시간이 너무 오래 걸림 -> 힙을 사용해야 함

import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) # heapq.heapify(데이터리스트): 힙 형태로 변경 (루트노드는 최솟값)
    
    while scoville[0] < K: # 최솟값이 K보다 작을 때 반복
        new_food = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_food) # heapq.heappush(힙, 넣을 데이터): 힙에 데이터를 push
        answer += 1
        
        # 길이가 1보다 작고(더 섞을 음식이 X), 최솟값이 K보다 작으면
        if len(scoville) == 1 and scoville[0] < K:
            return -1 # 만들 수 없는 경우
    
    return answer