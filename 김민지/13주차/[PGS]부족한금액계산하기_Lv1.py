def solution(price, money, count):
    answer = -1
    sp = 0            #sum_price
    for i in range(count):
        sp += price * (i+1)
        
    answer = sp - money
    if answer < 0:
        answer = 0

    return answer

#return max(0,price*(count+1)*count//2-money)