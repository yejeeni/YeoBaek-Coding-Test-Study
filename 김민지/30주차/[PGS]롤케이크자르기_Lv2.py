from collections import Counter

def solution(topping):
    answer = 0
    #딕셔너리로 전채 개수 파악
    right = Counter(topping)
    left = set()
    
    for t in topping:
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]     # 더 이상 없으면 제거
            
        if len(left) == len(right):
            answer += 1
        
    return answer


"""
def solution(topping):
    answer = 0
    for i in range(1, len(topping)):
        a = len(set(topping[:i]))
        b = len(set(topping[i:]))
        if a == b:
            answer += 1
        
    return answer
    
#매번 슬라이싱을 하게 돼서 100만개의 토핑에는 시간초과됨
"""