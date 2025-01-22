def solution(s):
    answer = ''
    
    check = 1 #대문자가 와야하는지 여부 / 맨 앞은 대문자이므로 초기설정 1
    
    for i in s:
        if i == ' ': #공백이라면...
            answer += i
            check = 1 #다음에 대문자 오도록 체크
            continue
        
        if check == 1:
            answer += i.upper() #맨 앞/ 공백 뒤에는 대문자로
            check = 0
        else :
            answer += i.lower() #그 외에는 소문자로
    
    return answer