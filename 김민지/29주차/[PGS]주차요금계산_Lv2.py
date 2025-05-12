import math
from collections import defaultdict
#fees = [기본시간, 기본요금, 단위시간, 단위요금]
#records = [시간, 번호, in/out]
#answer = 차량번호가 작은 자동차부터 청구할 금액
def solution(fees, records):
    answer = []
    기본시간, 기본요금, 단위시간, 단위요금 = fees
    
    r = {}
    t = defaultdict(int)
    
    for record in records:
        time, number, status = record.split()
        hour, minute = map(int, time.split(':'))
        total_time = hour*60 + minute
        
        if status == "IN":    #in인 경우 r에 차량번호, 들어온 시간 저장
            r[number] = total_time
        elif status == "OUT":  #out인 경우 차량 t에 차량번호, 머무른 시간 저장
            in_time = r.pop(number)
            t[number] += total_time - in_time   #2번 들어오는 경우도 고려
        #print(r , t)
    
    #r에 값이 남아있으면 out이 안된 차가 있는 것
    for number, in_time in r.items():     #out이 없는 경우 out을 23:59로 설정
        t[number] += (23 * 60 + 59) - in_time
        #print("no out", t)
        
    for number in sorted(t):
        time = t[number]
        if time <= 기본시간:  #시간이 기본시간보다 적으면 기본요금만
            fee = 기본요금
        else:                #아니면
            기본넘은시간 = time - 기본시간  #초과한 시간까지 계산
            fee = 기본요금 + math.ceil(기본넘은시간 / 단위시간) * 단위요금
            
        answer.append(fee)
        #print(answer)
        
        
    return answer