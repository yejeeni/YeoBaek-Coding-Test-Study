from itertools import product  #중복순열 생성

def solution(word):
    answer = 0
    alp = ['A', 'E', 'I', 'O', 'U']
    dic = []   #사전

    #모든 조합 생성
    for i in range(1, 6):
        for p in product(alp, repeat=i):
            dic.append(''.join(p))
    
    #사전 정렬
    dic.sort()
    answer = dic.index(word) + 1  #0부터 시작이므로 1더해줌
    
    return answer
"""
def solution(word):
    alp = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]  #5^0 + 5^1 + 5^2 + 5^3 + 5^4 = 781
    
    answer = 0
    for i, c in enumerate(word):
        idx = alp.index(c)              #알파벳이 몇번째 순서인지
        answer += idx * weights[i] + 1  #인덱스 만큼 점프 + 현재 글자 포함
    return answer

"""
"""
A AA AAA AAAA 
AAAAA AAAAE AAAAI AAAAO AAAAU
AAAE AAAEA AAAEE AAAEI AAAEO AAAEU
AAE AAEA AAE
"""