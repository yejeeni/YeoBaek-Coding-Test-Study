def solution(s, skip, index):
    answer = ''
    skip_list = []
    
    for i in skip:
        skip_list.append(ord(i))
        
    for i in s:
        cur = ord(i)
        count = 0
        while count < index:
            cur += 1
            
            if cur > 122:
                cur = 97

            if cur not in skip_list:
                count += 1
                
        answer += chr(cur)

    return answer

#아스키 97~122 소문자 알파벳
#count("해당")