def solution(arr1, arr2):
    answer = []
    
    #행렬의 곱 : 앞 행렬의 행 X 뒷 행렬의 열
    #          cf. (m X n 크기의 행렬) X (n X r 크기의 행렬) = m X r (크기의 행렬)
    
    m = len(arr1) #크기
    n = len(arr2)
    r = len(arr2[0])
    
    for col in range(m):
        row_list = [] #한 행씩 구하여 정답에 추가...
        
        for row in range(r):
            element = 0
            for i in range(n):
                element += arr1[col][i] * arr2[i][row] #원소의 값 구하기
            row_list.append(element) #행에 추가
        answer.append(row_list) #구한 행을 행렬에 추가
    
    return answer