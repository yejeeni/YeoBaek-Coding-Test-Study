def solution(ingredient):
    answer = 0
    tmp = []

    # 리스트의 요소를 하나씩 스택에 추가
    for item in ingredient:
        tmp.append(item)  # 현재 요소 추가

        if tmp[-4:] == [1, 2, 3, 1]:   #마지막 4개의 요소가 [1, 2, 3, 1]인지 확인
            answer += 1 
            del tmp[-4:] 

    return answer
#위의 경우에는 시간복잡도 O(N)
#최악의 경우 시간복잡도 O(N^2)  (아래)

"""
    i = 0
    while i <= len(ingredient) - 3: 
        if ingredient[i:i + 4] == [1, 2, 3, 1]:
            answer += 1
            del ingredient[i:i + 4]
            i = 0

        else:
            i += 1
"""