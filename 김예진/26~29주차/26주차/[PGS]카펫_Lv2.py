def solution(brown, yellow):
    
    for bh in range(1, brown//2 + 1): # 세로 길이는 가로 길이보다 작거나 같으므로 절반까지만 확인
        # 아래에서 계산한 수식을 이용하여 bw, yw, yh 계산
        bw = (brown - 2 * bh + 4) // 2
        yw = bw - 2
        yh = bh - 2
        
        # 노랑의 개수가 (노랑 가로) * (노랑 세로) 이고, 노랑 + 갈색이 (갈색 가로) * (갈색 세로) 가 맞는 경우
        if yellow == yw * yh and yellow + brown == bw * bh:
            return [bw, bh]

"""
    브라운의 가로 = brown_width = bw
    브라운의 세로 = brown_height = bh
    옐로우의 가로 = yellow_width = yw
    옐로우의 세로 = yellow_height = yh
    
    A. 브라운 가로, 브라운 세로 길이 = 옐로우 가로+2, 옐로우 세로+2
    bw, bh = yw + 2, yh + 2
    
    B. 브라운 개수 + 옐로우 수 = 카펫의 전체 크기 = 브라운 가로 x 브라운 세로
    brown + yellow = carpet = bw x bh = (yw + 2) x (yh + 2)
    
    C. 옐로우 = 옐로우 가로 x 옐로우 세로 
    yellow = yw x yh = (bw - 2) x (bh - 2)
    
    D. 브라운 = 브라운 가로 + 브라운 가로 + 브라운 세로 + 브라운 세로 - 4
    brown = bw + bw + bh + bh - 4 = 2bw + 2bh - 4
    
    따라서
    bw = (brown - 2bh + 4) / 2
    을 이용해보자. - 출처: https://aiday.tistory.com/137
"""