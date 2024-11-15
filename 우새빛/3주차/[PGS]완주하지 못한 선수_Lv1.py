def solution(participant, completion):
    hashdict = {}
    
    for p in participant:
        hashdict[p] = hashdict.get(p, 0) + 1
        #if p in hash: hash[p] += 1 / else: hash[p] = 1와 동일

    for c in completion:
        hashdict[c] -= 1
        if hashdict[c] == 0:
            del hashdict[c]
    
    return list(hashdict.keys())[0]

"""
1) 이중 for 문을 돌려 participant와 completion을 비교하여 찾기 -> O(N^2)
2) participant와 completion을 정렬한 후 차례대로 비교하여 찾기-> O(NlogN) = O(NlogN)(sort()) + O(N)(for문을 통해 비교)
3) 해시를 이용 -> O(N)
   내가 사용한 방법 - key : 사람 이름, value : 이름을 가진 사람 수 (동명이인이 있을 수 있음)
                   - dict에 participant 명단의 사람 추가 후 completion 명단의 사람 제거 -> 최종으로 남은 사람이 완주 못한 선수
   다른 사람들 방법 - key : hash(p), value : p
                   - dict에 participant 명단의 사람을 추가하며 hash(p)값의 총합을 구함
                     후에 completion 명단의 사람의 hash(p)값을 구한 총합에서 제거 -> 남은 hash값을 key값으로 가진 사람이 완주 못한 선수 

***해시를 써야할 때 : string 기반으로 정보를 기록하고 관리해야할 때
"""

def solution2(participant, completion):
    answer = ''
    temp = 0
    hashdict = {}
    
    for p in participant:
        hashdict[hash(p)] = p
        temp += int(hash(p))
        
    for c in completion:
        temp -= hash(c)
        
    answer = hashdict[temp]
    return answer