#예외 무수히 많이 발생... -> 완전 탐색 할 것
def solution(k, dungeons): #K:현재피로도 d:각 던전별"최소 필요 피로도", "소모 피로도"
    answer = 0
    
    dungeons.sort(key = lambda x : x[1]) #최소 필요 기준으로 내림차순 정렬
    
    for d in dungeons:
        if k >= d[0] :
            k -= d[1] #최소 필요 피로도 보다 현재 피로도가 높다면 피로도를 소모(던전 탐험)
            answer += 1
    
    return answer

#성공
from itertools import permutations

def solution2(k, dungeons):
    answer = -1
    
    #던전의 개수는 1이상 8이하 -> 순열로 모든 경우 나열
    d_case = [list(p) for p in permutations(dungeons, len(dungeons))]

    for dun in d_case:
        temp_k = k
        count = 0
        for d in dun:
            if temp_k >= d[0] :
                temp_k -= d[1] #최소 필요 피로도 보다 현재 피로도가 높다면 피로도를 소모(던전 탐험)
                count += 1
            
            if answer < count:
                answer = count
    
    return answer

#성공_다른 것은 동일... 순열 이터레이터를 반복문에서 바로 호출하는 것이 코드가 더 짧다.
def solution3(k, dungeons):
    answer = -1

    #던전의 개수는 1이상 8이하 -> 순열로 모든 경우 나열
    for p in permutations(dungeons, len(dungeons)): #p를 반복문에서 바로 생성
        temp_k = k
        count = 0
        for d in p:
            if temp_k >= d[0] :
                temp_k -= d[1] #최소 필요 피로도 보다 현재 피로도가 높다면 피로도를 소모(던전 탐험)
                count += 1
            
            if answer < count:
                answer = count
    
    return answer