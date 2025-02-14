def solution(board, moves):
    answer = 0
    basket = []
    bb = []
    board_t = list(map(list, zip(*board)))  # 전치행렬
    
    for b in board_t:
        b = list(filter(lambda x: x != 0, b))  #리스트의 모든 0제외
        bb.append(b)

    for m in moves:
        #print(bb[m-1])
        if not bb[m-1]:
            continue
        
        basket.append(bb[m-1][0])
        bb[m-1].pop(0)
        
        if len(basket) > 1 and (basket[-2] == basket[-1]):
            basket.pop()
            basket.pop()
            answer += 2   

    return answer

