def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1, c2 = 0, 0
    for g in goal:
        print(g)
        if c1 < len(cards1) and g == cards1[c1]: 
            c1 += 1
        elif c2 < len(cards2) and g == cards2[c2]:
            c2 += 1
        else:
            answer = 'No'
        print(c1, c2)
            
    return answer