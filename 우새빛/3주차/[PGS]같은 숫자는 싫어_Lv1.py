def solution(arr):
    answer = []
    temp = -1
    
    for i in arr:
        if i != temp: #앞의 숫자와 다르면 추가
            answer.append(i)
            temp = i
    
    return answer

"""
내가 사용한 방법 - temp에 앞의 숫자를 임시로 저장하여 동일(연속)인지 비교 후 리스트에 추가 
다른 사람들 방법 - 슬라이싱을 이용하여 리스트에 마지막으로 저장된 숫자와 비교 후 리스트에 추가
                  -> temp라는 변수를 사용하지 않아도 됨
"""

def solution2(arr):
    answer = []
    
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    
    return answer