def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total_p = 0 
        for t in target:    #타겟의 알파벳순서대로 비교
            min_p = float('inf')    #최솟값 설정해서
            for keys in keymap:     #keymap 순서대로 타켓 비교
                idx = keys.find(t)  
                if idx != -1:       #일치하는게 있으면
                    min_p = min(min_p, idx + 1)   #그중 가장 작은값 +1을 설정
            
            if min_p == float('inf'):      #일치하는게 모든 keymap에 다 없으면
                total_p = -1               #이 타겟은 완성될 수 없음
                break
            
            total_p += min_p  #아니면 min을 계속 total에 누적
        
        answer.append(total_p)
    return answer

#시간복잡도는 O(MxNxKxL)
#keymap의 철자들의 최소횟수를 다 구하고 target과 비교하는 식으로 하면 시간복잡도 낮아짐