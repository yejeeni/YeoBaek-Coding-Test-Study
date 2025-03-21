def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):   #최대와 최소를 서로 곱하면 됨
        answer += A[i]*B[i]
    return answer

#Max, Min함수를 이용해서 하여 곱의 합을 저장하고 remove로 값을 삭제하는 식으로 진행하였으나
#O(N^2)의 복잡도로 효율성이 안좋음
#따라서 미리 정렬을 하고 곱하는 식으로 변경하여 O(N logN)의 복잡도가 됨