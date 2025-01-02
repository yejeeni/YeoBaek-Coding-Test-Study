from collections import deque
def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # ▲(A에서 다음 알파벳으로) / ▼(Z로 이동 후 이전 알파벳으로) 둘 중 최소값 찾기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 실시간 좌우 조작
        right = i + 1
        while right < len(name) and name[right] == 'A':
            right += 1
            
        # 3가지 중 최단 경로를 갱신
        min_move = min([min_move, 2 * i + len(name) - right, i + 2 * (len(name) -right)])
        
    answer += min_move
    return answer