from collections import Counter

def solution(N, stages):
    answer = []
    stg_count = Counter(stages)  # 각 스테이지에 머물러 있는 사람 수 카운팅
    fail_list = []
    clear = len(stages)  # 현재 도달한 플레이어 수

    for i in range(1, N + 1):
        if clear > 0:  # 나눗셈 방지 (스테이지에 도달한 사람이 없으면 0)
            fail_rate = stg_count[i] / clear
        else:
            fail_rate = 0
        
        fail_list.append((fail_rate, i))  # (실패율, 스테이지 번호) 저장
        clear -= stg_count[i]  # 다음 스테이지 도달자 수 갱신

    # 실패율 기준으로 정렬 (실패율이 같다면 스테이지 번호 오름차순)
    fail_list.sort(key=lambda x: (-x[0], x[1]))
    answer = [stage for _, stage in fail_list]  # 스테이지 번호만 추출

    return answer



"""
# 스테이지 도달, 클리어x / 스테이지 도달 = 실패율
def solution(N, stages):
    answer = []
    stg = [0 for _ in range(N+1)]
    fail_list = [0 for _ in range(N+1)]
    
    for s in stages:
        stg[s-1] += 1
    
    clear = len(stages)
    for i in range(N):
        
        fail_list[i] = stg[i] / clear
        
        clear -= stg[i]

    fail_list.pop()
    sort = sorted(range(len(fail_list)), key=lambda i: fail_list[i], reverse=True)

    answer = [i + 1 for i in sort]
    
    return answer
"""