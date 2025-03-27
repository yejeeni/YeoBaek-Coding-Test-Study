from collections import Counter
def solution(k, tangerine):
    c = sorted(Counter(tangerine).values(), reverse=True)
    get = 0
    var = 0
    for n in c:
        get += n
        var += 1
        if get >= k:  # k개를 채우면 종료
            break
        
    return var