from collections import deque

def solution(maps):
    n = len(maps)          #행
    m = len(maps[0])       #열
    
    #이동 방향: x -1(위) / x +1(아래) / y -1(왼) / y +1(오)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))  #큐 초기화 / 시작은 0,0
    
    while queue:
        x, y = queue.popleft()  #현재위치
        
        for i in range(4):  #상하좌우로 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m: #맵 벗어남
                continue
            
            if maps[nx][ny] == 0:              #벽이거나 갔던 곳
                continue
            
            if maps[nx][ny] == 1:              #처음이면 
                maps[nx][ny] = maps[x][y] + 1  #몇번째 순서에 들렸는지
                queue.append((nx, ny))         #간 곳을 queue에 추가
            
    
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1  #맵의 제일 끝 값이 1이면 도착 못한거