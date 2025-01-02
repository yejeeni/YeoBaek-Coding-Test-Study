def solution(park, routes):
    answer = []
    
    height = len(park) #전체 공원의 높이와 넓이 구하기
    width = len(park[0])
    
    locs = [] #시작 좌표와 장애물이 있는 좌표 구하기 locs(높이, 넓이)
    hurdle = []
    for h, ppp in enumerate(park):
        for w, p in enumerate(ppp):
            if p == 'S':
                locs = [h, w]
            if p == 'X':
                hurdle.append([h, w])  
    
    temp = [] #진행 할 수 있는 경로인지 판단 후 이동
    for route in routes:        
        dir, dist = route.split()
        dist = int(dist)
        #판단을 위해 진행 했을 경우의 좌표 임시로 구하기
        if dir == 'N':
            temp = [locs[0]-dist, locs[1]]
        elif dir == 'S':
            temp = [locs[0]+dist, locs[1]]
        elif dir == 'W':
            temp = [locs[0], locs[1]-dist]
        elif dir == 'E':
            temp = [locs[0], locs[1]+dist]
        
        #조건 확인1 (공원을 벗어나는지 확인)
        if (temp[0]<0 or temp[0]>height-1) or (temp[1]<0 or temp[1]>width-1):
            continue
        
        #조건 확인2 (장애물을 만나는지 확인)
        check = False
        for h in hurdle:
            if (dir == 'N' and locs[0] > h[0] >= temp[0] and locs[1] == h[1]) or \
               (dir == 'S' and locs[0] < h[0] <= temp[0] and locs[1] == h[1]) or \
               (dir == 'W' and locs[1] > h[1] >= temp[1] and locs[0] == h[0]) or \
               (dir == 'E' and locs[1] < h[1] <= temp[1] and locs[0] == h[0]):
                    check = True
                    break
        if check == True:
            continue
        
        #조건에 걸리지 않는다면 이동 좌표로 수정
        locs = temp
    return locs