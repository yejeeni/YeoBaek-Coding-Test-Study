def solution(s):
    answer = ''
    
    s_list = list(map(int, s.split(" ")))
    res = []
    res.append(str(min(s_list)))
    res.append(str(max(s_list)))
    
    answer = " ".join(res)
    return answer