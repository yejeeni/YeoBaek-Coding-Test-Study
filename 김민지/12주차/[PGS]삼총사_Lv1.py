from itertools import combinations

def solution(number):
    answer = 0

    #순서대로 123...을 매겨서 이 순서가 3가지 조합을 가짐
    clist = list(combinations(range(len(number)), 3))
    print(clist)

    #순서가 가지는 값으로 다시 조합 생성
    for comb in clist:
        n = []
        for i in comb:
            n.append(number[i])   #순서에 해당하는 값을 n에 추가
        if sum(n) == 0:      #n값의 합이 0이 되면 answer +1 해줌
            answer += 1
            
    return answer

#시간복잡도 O(N^3)