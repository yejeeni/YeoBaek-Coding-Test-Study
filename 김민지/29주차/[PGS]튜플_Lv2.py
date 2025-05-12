import re

def solution(s):  #s는 문자열
    # 중괄호 안의 숫자 묶음 찾아냄
    sets = re.findall(r'\{([\d,]+)\}', s)
    # 문자열 집합을 정수 리스트로 변환
    sets = [list(map(int, group.split(','))) for group in sets]
    # 집합들을 길이 기준으로 정렬
    sets.sort(key=len)
    
    answer = []
    seen = set()
    
    for group in sets:
        for num in group:
            if num not in seen:  #기존에 나왔는지 아닌지 확인
                answer.append(num)  #안나왔으면 answer에 추가하고
                seen.add(num)       #확인에도 추가해줌
                break           #한 set에서 하나씩만 추가됨
    
    return answer