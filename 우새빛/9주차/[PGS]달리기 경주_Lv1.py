def solution(players, callings): #테스트7 ~ 13 시간초과
    
    for c in callings:
        for i, p in enumerate(players):
            if p == c:
                players[i] = players[i-1]
                players[i-1] = p
    
    return players

#시간초과가 가는 이유 예상 : 추월한 선수를 리스트에서 찾는데 오래걸리기 때문에
#-> 해시를 이용하자자

def solution2(players, callings): #통과
    
    ranking = {} #현재 랭킹 정보를 담은 해시 생성
    for i, p in enumerate(players):
        ranking[p] = i
    
    for c in callings:
        current_rank = ranking[c] #현재 추월한 선수의 순위 찾기
        
        temp = players[current_rank - 1] #랭킹 업데이트
        ranking[temp] += 1
        ranking[c] -= 1
        
        players[current_rank] = players[current_rank - 1] #순위 교체
        players[current_rank - 1] = c
        
    return players