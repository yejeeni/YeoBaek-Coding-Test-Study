def solution(s):
    answer = True
    tmp = []
    if s[0] == ")": return False  #시작부터 실패
    
    for i in range(len(s)):
        tmp.append(s[i])
        if len(tmp) >= 2 and tmp[-2] == "(" and tmp[-1] == ")":
            tmp.pop()
            tmp.pop()

    if len(tmp) > 0: answer = False  #tmp에 남아 있으면 실패
    return answer