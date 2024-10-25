s="(())))" #false
def solution(s):
    answer = True

    temp = []
    if s[0] == ')':
        answer = False
    temp.append(s[0]) 
    for i in range(1, len(s)):
        temp.append(s[i]) #일단 넣고
        if temp[-1] == ')':
            if len(temp) > 1 and temp[-2] == '(': #두개가 쌍으로맞으면 제거함
                temp.pop()
                temp.pop()

    if len(temp) != 0: #스택이 다 비어있어야 괄호들이 다 짝으로 맞는거
        answer = False

    return answer
solution(s)