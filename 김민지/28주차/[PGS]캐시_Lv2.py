from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0
    
    for city in cities:         #cache hit
        city = city.lower()     # 대소문자 구분 없음 (문제 조건에 따라)
        
        if city in cache:
            cache.remove(city)  # 기존 걸 삭제하고
            cache.append(city)  # 최신으로 다시 추가
            time += 1          
            
        else:                            #cache miss
            if len(cache) >= cacheSize:
                if cache:
                    cache.popleft()      #오래된 것 제거(LRU)
            if cacheSize > 0:
                cache.append(city)       #새로 추가
            time += 5               
            
        
    return time