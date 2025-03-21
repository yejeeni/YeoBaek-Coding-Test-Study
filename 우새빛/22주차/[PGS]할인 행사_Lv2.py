def solution(want, number, discount):
    answer = 0
    
    for case in range(len(discount)-9): #가능한 10일 연속의 경우
        shop_list = dict(zip(want, number)) #dict 초기화
        
        for i in range(10): #연속 10일 카운트
            dis = discount[case+i]
            if dis in shop_list: 
                shop_list[dis] -= 1 #할인 물품이 구매리스트에 있다면 -1
                if shop_list[dis] == 0:
                    del shop_list[dis] #모두 샀다면 리스트에서 제거
                    
        if len(shop_list) == 0:
            answer += 1 #모두 구매했다면 카운트 추가
    
    return answer