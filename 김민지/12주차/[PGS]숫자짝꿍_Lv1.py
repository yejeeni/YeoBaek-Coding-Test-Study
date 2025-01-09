from collections import Counter

def solution(X, Y):
    answer = ''
    save = []

    yc = Counter(Y)
    
    for x in X:
        if yc[x] > 0:
            save.append(x)
            yc[x] -= 1

    save.sort(reverse=True)

    for s in save:
        answer = answer + s

    if not save:
        answer = '-1'
    if set(save) == {'0'}:
        answer = '0'
    
    return answer

#시간복잡도 O(x길이 + y길이 + NlogN)

"""  시간복잡도가 미친듯이 높게 나옴
    answer = ''
    save = []
    Y = list(Y)
    
    for x in X:
        if x in Y:
            save.append(x)
            Y.remove(x)

    save.sort(reverse=True)

    for s in save:
        answer = answer + s

    if not save:
        answer = '-1'
    if set(save) == {'0'}:
        answer = '0'
    
"""