def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n + 1  # 배열에서 행 번호
        col = i % n + 1   # 배열에서 열 번호
        answer.append(max(row, col))  
        
    return answer

#처음에는 이중for문을 이용하여 모든 값을 1차원 리스트로 저장하고 슬라이싱으로 하였으나 시간초과됨
#따라서 left부터 right부분만 행렬로 계산되도록 변경

#  (1,1) 1 | (1,2) 2 | (1,3) 3    
#  (2,1) 2 | (2,2) 2 | (2,3) 3
#  (3,1) 3 | (3,2) 3 | (3,3) 3 
# 이므로 행렬중에 큰 값으로 하면 됨