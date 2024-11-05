    
def solution(park, routes):
    answer = []   
    s_h = 0
    s_w = 0
    #시작점 위치 찾기
    for i in range(len(park)):
        if park[i].find("S") > 0:
            s_h = i
            s_w = park[i].find("S")
    print(s_h, s_w)
    
    goes = {"E":[0, 1], "W":[0, -1], "S":[1, 0], "N":[-1, 0]}

    
    for route in routes:
        go = int(route.split()[1])
        way = route.split()[0]
        do = True
        
        hh, ww = s_h, s_w   #임의좌표 업데이트
        
        print(way, go)
        
        for a in range(go):     #한칸 이동
            hh += goes[way][0]
            ww += goes[way][1]   
            
            if not (0 <= hh < len(park) and 0 <= ww < len(park[0])) or park[hh][ww] == "X":
                do = False
                break
            
            #if문에 안걸리면 s_h, s_w 변경
        
        if do == True:
            s_h = hh
            s_w = ww
        print(s_h, s_w)
        
    answer.append(s_h)
    answer.append(s_w)
        
    
        
    return answer