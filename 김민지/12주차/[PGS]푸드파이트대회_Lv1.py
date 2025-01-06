def solution(food):
    answer = ''
    count = 0
    for f in food:
        if f == 1:   #f값이 1인 경우 count 1증가하고 넘어가기
            count += 1
            continue
            
        f = f//2         #2로 나눈 정수값을 for 문을 사용해서 answer에 추가해주기
        for i in range(f):
            answer = answer + str(count)
        count += 1
    
    a = answer
    answer += '0'          #중간에 물
    answer = answer + a[::-1] #역순도 합해주기
    return answer