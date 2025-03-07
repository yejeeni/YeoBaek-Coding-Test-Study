def solution(nums):
    answer = 0
    n = set(nums)   #set으로 종류 수 구함

    if (len(nums) / 2) > len(n):  #(len(nums) / 2)는 뽑는 수
        answer = len(n)
    elif (len(nums) / 2) <= len(n):
        answer = (len(nums) / 2)
        
    return answer

"""
뽑을 수 있는 최대 종류를 구해야함

뽑는 수가 종류수보다 적으면 뽑는 수가 최대 종류
뽑는 수가 종류수보다 많으면 종류수가 최대종류
"""