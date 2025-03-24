import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  #힙 변환
    answer = 0

    while 1: 
        a = heapq.heappop(scoville)  #제일 안매운거
        if a >= K:        #제일 작은 값이 k보다 크면 바꿀필요 없음
            break
        if len(scoville) < 1:    #길이가 1이 안되면 -1반환
            return -1
        b = heapq.heappop(scoville)  #두번째로 매운거
        new = a + b * 2
        heapq.heappush(scoville, new)   #새로운 값을 heap에 추가
        answer += 1

    return answer

#O(NlogN)