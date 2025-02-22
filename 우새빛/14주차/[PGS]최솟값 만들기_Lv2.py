from itertools import permutations

def solution(A,B): #테스트 1제외 모두 시간초과과
    f = 0
    answer = 10000000

    A_case = [list(p) for p in permutations(A, len(A))] #A의 순열
    
    for i in range(len(A_case)):
        temp = 0
        for j in range(len(A_case[0])): #A의 순열 중 하나와 B를 계산해 최소값 직접 계산...
            temp += A_case[i][j] * B[j]
        if f == 0:
            answer = temp
            f = -1
        elif answer > temp:
            answer = temp
    return answer
#순열을 다 돌려 직접 계산하기에는 너무 오래 걸리는 것으로 예상

def solution(A,B):
    answer = 0
    
    #A의 가장 큰 값과 B의 가장 작은 값, A의 가장 작은 값과 B의 가장 큰 값을 곱하여
    #더하는 것이 곱의 합을 더했을 때 가장 값이 적을 것으로 예상
    A.sort()
    B.sort(reverse = True)
    
    for k in range(len(A)):
        answer += A[k] * B[k]
    
    return answer