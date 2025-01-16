def solution(brown, yellow):
    answer = []
    
    """
    □ □ ◪  brown는 카펫의 테두리 조각
    □   ■  -> 가로 + 세로 = brown + 1(◿로 나뉘므로) + 1(코너에 있는 것은 가로, 세로 모두 적용)
    ◪ ■ ■
    """
    
    sum_wh = brown / 2 + 2
    width = sum_wh // 2 #(기본값) 가로와 세로가 1:1로 설정
    if sum_wh % 2 != 0: #단, 딱 나누어떨어지지 않으면 가로>세로 이므로 가로에 +1
        width += 1
    height = sum_wh - width
    
    print(width, height)
    
    while True:
        if width * height == brown + yellow: #넓이를 이용하여 가로세로가 맞는지 확인
            break
            
        width += 1 #맞지 않다면 1씩 조정
        height -= 1
    
    #가로, 세로 크기를 순서대로 배열에 담아 return
    answer = [width, height]
    
    return answer