a=[1,2,3,4]
b=[-3,-1,0,2]
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
solution(a,b)