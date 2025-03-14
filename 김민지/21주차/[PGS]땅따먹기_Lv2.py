def solution(land):
    for i in range(1, len(land)):  # 두 번째 행부터 시작
        for j in range(4):  # 4개의 열을 탐색
            # 현재 칸 land[i][j]에 이전 행에서 같은 열을 제외한 최댓값 더하기
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[-1])  # 마지막 행에서 최댓값 찾기


#DP(동적계획법)