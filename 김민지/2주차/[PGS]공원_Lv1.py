def solution(mats, park):  
    answer = 0
    park_c = len(park)      #공원의 세로길이 (행)
    park_r = len(park[0])   #공원의 가로길이 (열)
    max_size = 0

    #최대 정사각형 찾기
    for c in range(park_c):
        for r in range(park_r):
            
            if park[c][r] == "-1":
                #print("find null")
                count = 0
                sq = True
                
                while(sq):
                    count += 1   
                    if r + count > park_r or c + count > park_c:   #만약 범위를 벗어나게 된다면 break
                        sq = False
                        break
                    
                    for i in range(count):
                        for j in range(count):
                            
                            if park[c + i][r + j] != "-1":
                                sq = False
                                break
                                
                        if not sq:   #반복문 빠져나오기
                            break

                    if sq:
                        max_size = max(max_size, count)

                    print(max_size)
                    
    #돗자리 크기와 비교하기
    for mat in mats:
        if mat <= max_size:
            answer = max(answer, mat)
    if answer == 0:
        answer = -1
            
        print(answer)

    
    return answer