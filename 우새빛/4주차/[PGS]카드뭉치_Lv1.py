def solution(cards1, cards2, goal):
    answer = ''
    
    #두 카드 뭉치의 번째 수를 달리 카운트
    #해당 번째 카드와 goal의 문장 비교
    num1 = 0; num2 = 0
    
    for g in goal:
        if (num1 < len(cards1)) and (cards1[num1] == g): #비교 전 리스트의 범위와 비교 (인덱스 에러 방지)
            num1 += 1                                    #비교 후 가능한 카드가 있으면 카운트
        elif (num2 < len(cards2)) and (cards2[num2] == g):
            num2 += 1
        else :                                           #카드를 비교하여 가능하지 않다면 No 전달
            answer = 'No'
            return answer
        
    answer = 'Yes'
    return answer

def solution2(cards1, cards2, goal): #다른 사람 풀이, POP 이용 -> 변수가 더 적다.
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"