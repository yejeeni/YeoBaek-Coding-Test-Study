def solution(n):
    answer = 0
    
    for i in range(1, n//2+1): #1~n의 반까지를 시작으로
        num = i
        sum_num = 0
        while sum_num <= n:
            sum_num += num #연속하는 수를 계속 더해보기
            if sum_num == n: #이때 n과 같으면 answer +1
                answer += 1
                break
            num += 1
            
    answer += 1 #n=n
    return answer