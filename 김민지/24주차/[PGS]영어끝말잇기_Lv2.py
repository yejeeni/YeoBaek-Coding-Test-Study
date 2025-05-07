def solution(n, words):
    answer = [0, 0]
    used_words = {words[0]}  # 중복 체크를 위한 집합 사용
    
    for i in range(1, len(words)):
        if words[i] in used_words or words[i][0] != words[i-1][-1]:  # 중복되거나 끝말잇기 규칙 어길 경우
            answer = [(i % n) + 1, (i // n) + 1]
            break
        
        used_words.add(words[i])
        

    return answer