def solution(s):
    answer = []
    is_list = []
    
    for idx, i in enumerate(s):
        if i not in is_list:
            answer.append(-1)
        else:
            prev_idx = is_list.index(i)    # 이전 위치 찾아오기
            answer.append(idx - prev_idx)  # 거리 계산
            is_list[prev_idx] = None       # 중복 방지
        is_list.append(i)
    return answer