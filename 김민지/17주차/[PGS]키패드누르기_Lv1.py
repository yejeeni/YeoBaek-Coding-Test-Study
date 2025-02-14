def solution(numbers, hand):
    answer = ''
    
    # 각 숫자에 대한 좌표 정의
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)  # 0의 좌표는 (3, 1)
    }
    
    # 시작 위치: 왼쪽 손은 * (3, 0), 오른쪽 손은 # (3, 2)
    l_pos = (3, 0)  # 왼손 시작 위치
    r_pos = (3, 2)  # 오른손 시작 위치
    
    for num in numbers:
        if num == 0:
            num = 0  # 0은 그대로 처리
            
        # 왼쪽 열(1, 4, 7)에 있는 숫자는 왼손
        if num in [1, 4, 7]:
            answer += 'L'
            l_pos = keypad[num]
        
        # 오른쪽 열(3, 6, 9)에 있는 숫자는 오른손
        elif num in [3, 6, 9]:
            answer += 'R'
            r_pos = keypad[num]
        
        else:
            # 가운데 열에 있는 숫자 (2, 5, 8, 0)
            # 각 손의 거리 계산
            l_len = abs(l_pos[0] - keypad[num][0]) + abs(l_pos[1] - keypad[num][1])
            r_len = abs(r_pos[0] - keypad[num][0]) + abs(r_pos[1] - keypad[num][1])
            
            # 더 가까운 손가락 사용
            if l_len < r_len:
                answer += 'L'
                l_pos = keypad[num]
            elif l_len > r_len:
                answer += 'R'
                r_pos = keypad[num]
            elif l_len == r_len:
                # 거리가 같으면 손잡이에 따라 결정
                if hand == "left":
                    answer += 'L'
                    l_pos = keypad[num]
                else:
                    answer += 'R'
                    r_pos = keypad[num]
        
    return answer