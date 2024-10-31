def solution(n, m, section):
    count = 0  
    pos = 0    # 현재 페인트칠된 마지막 구역
    
    for sec in section:
        if sec > pos:     # 롤러 칠하지 못하면 sec은 pos보다 큼
            count += 1   
            pos = sec + m - 1  #마지막 구역 업데이트
            
    return count