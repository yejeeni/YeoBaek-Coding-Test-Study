def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                print("find", i, j)
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i+1)
                rdy = max(rdy, j+1) 
    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)

        
    return answer