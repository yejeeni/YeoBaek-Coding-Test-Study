import heapq #heapq 모듈에서 힙(min-heap) 지원

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) #heap = heapq.heapify(scoville)는 불가능 
                            #heapq.heapify() 함수는 리스트를 변경, 반환값은 없음. 위의 결과는 heap = None이 됨
    
    while True:
        if scoville[0] >= K: #모든 음식의 스코빌 지수가 K이상인지 확인 (최소값이 k보다 크다면 성립)
            break           #이때, heap[0]은 root 값, min_heap이므로 root가 항상 최소값
            
        if len(scoville) <= 1: #섞기에 앞서 개수가 1개뿐이면 불가능
            answer = -1
            break
        
        answer += 1 #섞는 횟수 +1
        
        fst_min = heapq.heappop(scoville) #스코빌 지수 낮은 수 추출
        snd_min = heapq.heappop(scoville)
    
        new = fst_min + (snd_min * 2) #섞은 음식의 스코빌 지수 구해서 힙에 추가
        heapq.heappush(scoville, new)
        
    return answer


#테스트 18 실패 -> 섞지 않아도 가능한 경우로 추측 / if ~ break의 위치를 재설정하여 해결...