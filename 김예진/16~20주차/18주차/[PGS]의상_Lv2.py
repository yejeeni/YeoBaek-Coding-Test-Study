# 얼굴, 상의, 하의, 갑옷 별 최대 1가지만 가능
# 하루에 최소 1개 이상의 옷

def solution(clothes):
    answer = 1
    
    dic = {}
    
    # 의상 종류 별 개수를 카운트
    # 딕셔너리에 있으면 +1, 없으면 1
    for cloth, category in clothes:
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
            
    # 의상 조합 계산 
    for key, value in dic.items():
        answer *= (value+1)
    
    return answer-1 # 아예 안입는 건 제외