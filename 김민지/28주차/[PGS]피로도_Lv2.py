from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons):   #모든 경우를 다 돌림
        피로도 = k
        count = 0
        for 최소필요, 소모 in p:
            if 피로도 >= 최소필요:    #되는 경우에 conut증가
                피로도 -= 소모
                count += 1
            else:              #안되는 경우에는 빠져나옴
                break
        answer = max(answer, count) #되는경우 answer에 저장 / 다음에 더 큰 conut 나오면 바꿈
        
    return answer