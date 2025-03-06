import collections

def solution(participant, completion):
    # p_dict = collections.Counter(participant)
    # c_dict = collections.Counter(completion)
    
    # result = p_dict - c_dict
    
    # return list(result.keys())[0]  
      
    dic = {} # 참가자 명단
    
    # 참가자 카운트
    for p in participant:
        if p not in dic: # 이름이 처음 나오는 경우
            dic[p] = 1 # 키-밸류 : 이름-1명
        else: # 동명이인이 있는 경우
            dic[p] += 1 # 해당 이름 +1명
    
    # 완주자 카운트
    for c in completion:
        dic[c] -= 1
        
    for key, value in dic.items(): # 딕셔너리의 키와 값을 items()로 순회
        if value > 0:
            return key
    