def solution(clothes):
    answer = 0
    
    clothes_type = {}
    
    # 옷 종류 별로 몇 개씩 있는지 카운트하기
    for name, type in clothes:
        if type not in clothes_type:
            clothes_type[type] = 0;
        clothes_type[type] += 1
    
    # 해당 타입의 옷을 입지 않는 것을 포함하여 코디 경우의 수 구하기
    answer = 1
    for i in clothes_type:
        answer *= (clothes_type[i] + 1)
    # 단 모두 입지 않는 경우는 제외
    answer -= 1
    
    return answer