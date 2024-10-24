A=[1, 2]
B=[3, 4]
def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
solution(A,B)