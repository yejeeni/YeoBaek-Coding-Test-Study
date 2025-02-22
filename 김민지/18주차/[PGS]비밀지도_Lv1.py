def solution(n, arr1, arr2):
    answer = []
    array1 = []
    array2 = []

    for a1 in arr1:
        a = format(a1, f'0{n}b')
        array1.append(a)

        
    for a2 in arr2:
        a = format(a2, f'0{n}b')
        array2.append(a)

    print(array1)
    print(array2)
    
    for i in range(len(array1)):
        row = ""  # 한 줄의 결과를 저장할 변수
        for j in range(n):  # 
            if array1[i][j] == "1" or array2[i][j] == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)
    print(answer)
    return answer

#시간복잡도 O(n * n)

