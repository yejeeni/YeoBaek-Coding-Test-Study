def solution(babbling):
    answer = 0
    wlist = ["aya", "ye", "woo", "ma"]    
    
    for b in babbling:
        is_valid = True  # 유효성 확인 변수
        prev_word = ""
        
        while b:
            matched = False  # 현재 단어 매칭 여부
            
            for word in wlist:
                if b.startswith(word) and word != prev_word:  
                    b = b[len(word):]  # 단어 제거
                    prev_word = word   # 이전 단어 갱신
                    matched = True     # 단어가 겹쳤다면 그 단어 빼고 다시 확인
                    break
                    
            if not matched:      # 어떤 단어도 겹치지 않으면 안되는거
                is_valid = False  
                break
        
        if is_valid and not b:  # 유효하고 문자열이 비었으면 카운트 증가
            answer += 1
    
    return answer

#시간복잡도 O(NxM)