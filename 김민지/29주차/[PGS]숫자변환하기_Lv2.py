from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0))  # (현재 숫자, 연산 횟수)
    v = set()
    v.add(x)
    
    while q:
        curt, cnt = q.popleft()  #큐 제일 왼쪽 꺼냄
        
        if curt == y:   #현재 보는 수가 목표수면 끝
            return cnt

        for nxt in [curt + n, curt * 2, curt * 3]:  #3가지 연산
            #print("next", next_num)
            if nxt <= y and nxt not in v:   #y보다 작고 한번도 없었던 수만
                v.add(nxt)                       #있었다고 표시
                q.append((nxt, cnt + 1))   #큐에 추가해주기
        

    return -1  #아무것도 안되면 -1

# x + n / x * 2 / x * 3
# x -> y가 되는데 결리는 연산 횟수