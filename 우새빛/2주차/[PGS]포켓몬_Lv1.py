def solution(nums):
    answer = 0
    
    pocketmon = set(nums) #포켓몬의 종류들만
    if len(pocketmon) >= (len(nums)/2):
        answer = len(nums)/2
    else:
        answer = len(pocketmon)
    
    return answer

def solution2(nums):
    return min(len(nums)/2, len(set(nums)))
           #min 함수를 이용하면 코드의 수를 줄일 수 있음...