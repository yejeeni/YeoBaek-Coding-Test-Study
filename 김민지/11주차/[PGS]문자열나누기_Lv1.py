def solution(s):
    answer = 0
    x = s[0]  
    x_num = 1 
    nx_num = 0  

    for i in range(1, len(s)):  
        if s[i] == x: 
            x_num += 1
        else:  
            nx_num += 1

        if x_num == nx_num:
            answer += 1 
            if i + 1 < len(s):  # 다음이 남았다면
                x = s[i + 1]
            x_num = 0            # 새 구간 시작
            nx_num = 0

    # 마지막 구간이 남아있다면 처리
    if x_num != 0 or nx_num != 0:
        answer += 1
        
    return answer