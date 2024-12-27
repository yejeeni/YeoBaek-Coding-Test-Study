def solution(s):
    
    #(가 있으면 보관
    #)가 있으면 제일 최근 (와 짝임 -> 제일 최근거 꺼내기
    #보관된 (가 없거나 )가 남지 않으면 올바른 짝
    
    op_parenthesis = []
    
    for i in s:
        if i == ')':
            if len(op_parenthesis) <= 0: return False #(가 없음
            op_parenthesis.pop()
        if i == '(':
            op_parenthesis.append(i)
    if len(op_parenthesis) > 0: return False #(가 남음

    return True