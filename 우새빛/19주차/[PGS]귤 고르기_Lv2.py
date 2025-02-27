from collections import defaultdict

def solution(k, tangerine): #테스트 27~30, 33, 34 시간초과
    answer = 0
    
    #count_list = [0] * (max(tangerine) + 1) #리스트 선언
    count_list = defaultdict(int)  #기본값이 0인 딕셔너리 선언
    
    for t in tangerine:
        count_list[t] += 1 #각 숫자가 몇번 있는지 카운트
    
    while k > 0:
        #max_value = max(count_list)  #최대값
        #max_index = count_list.index(max_value) #최대값 인덱스
        max_key = max(count_list, key=count_list.get)
        
        k -= count_list[max_key] #가장 개수가 많은 수부터 소모하기
        count_list[max_key] = 0
        answer += 1
    
    return answer
#-> 최대값 찾는 것이 오래 걸리는 것으로 추정... 이를 빨리 해결하기 위해 heap 사용

#from collections import defaultdict
import heapq

def solution(k, tangerine):
    answer = 0
    count_list = defaultdict(int)  # 기본값이 0인 딕셔너리
    
    for t in tangerine:
        count_list[t] += 1 #각 숫자가 몇번 있는지 카운트
    
    heap = []
    for key, count in count_list.items():
        heapq.heappush(heap, (-count, key))  #개수를 음수로 넣어 가장 큰 값이 root로 오도록
    
    while k > 0:
        count, key = heapq.heappop(heap)  #최대값
        count = -count  #(count 양수로 바꿈)
        
        k -= count  #가장 개수가 많은 수부터 소모하기
        answer += 1
    
    return answer