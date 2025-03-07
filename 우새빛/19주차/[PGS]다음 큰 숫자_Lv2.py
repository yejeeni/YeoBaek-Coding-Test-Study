"""
(추가로 작성해 본 2진수 구하는 식)
def binary_number(n):
    list_num = []
    
    while n > 0:
        rem = n % 2
        n //= 2
        list_num.append(rem)
    
    return int("".join(map(str, list_num[::-1]))) #역순으로 조합하며 반환

def binary_number2(n): #bin함수를 이용하며 쉽게 구할 수 있음
    return int(bin(n)[2:])  #접두사(0b)를 제거하고 정수로 변환
"""

def count_ones(n):
    count = 0
    list_num = []
    
    while n > 0:
        rem = n % 2
        n //= 2
        
        if rem == 1:
            count += 1 #2진수로 변환시 1이면 카운트
    
    return count

def solution(n):
    
    n_ones = count_ones(n) #n을 2진수로 변환했을 떄 1의 개수
    
    big_num = n + 1 #다음 큰 숫자 1씩 더해가며 비교
    while True:
        if n_ones == count_ones(big_num): #만약 다음 큰 숫자가 2진수로 변환했을 때 1의 갯수가 같다면 종료
            break
        
        big_num += 1 #아니라면 1추가하여 다음 자연수 비교
    
    return big_num