def solution(s):
    answer = 0
    stack = []
    
    for i in s:
        stack.append(i)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        answer = 1

    return answer