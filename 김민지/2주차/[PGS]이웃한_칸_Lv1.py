def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0] 
    dw = [1, 0, 0, -1] 
    
    for i in range(4):
        hh = h + dh[i]
        ww = w + dw[i] 
        if -1<hh<len(board) and -1<ww<len(board[0]):  #범위 안의 경우만 판단
            if board[h][w] == board[hh][ww]:          #색이 동일하면 +1
                answer += 1
            
    return answer

