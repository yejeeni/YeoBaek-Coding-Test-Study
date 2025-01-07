def solution(keymap, targets):
    answer = []
    dict_key = {}
    
    # 각 알파벳를 최대한 적게 누르는 횟수 구하기
    for key in keymap:
        for k_num, k in enumerate(key):
            if k in dict_key:
                dict_key[k] = min(dict_key[k], k_num+1)
            else :
                dict_key[k] = k_num+1
    
    # 사전에 구한 횟수를 통해 누를 자판 수 구하기
    for target in targets:
        total_press = 0
        for t in target:
            if t not in dict_key:
                total_press = -1; break
            total_press += dict_key[t]
        answer.append(total_press)
    
    return answer