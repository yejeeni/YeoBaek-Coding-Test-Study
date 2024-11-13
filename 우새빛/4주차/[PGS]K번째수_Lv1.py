def solution(array, commands):
    answer = []
    
    for c in commands:
        temp = []
        for i in range(len(array)):
            if i >= c[0]-1 and i<c[1]:
                temp.append(array[i])
        temp.sort()
        answer.append(temp[c[2]-1])
        
    return answer

def solution2(array, commands):
    answer = []
    
    for i, j, k in commands:
        temp = array[i-1:j] #***인덱스 슬라이싱 사용 (다른 것은 위와 동일)
        temp.sort()
        answer.append(temp[k-1])
        
    return answer