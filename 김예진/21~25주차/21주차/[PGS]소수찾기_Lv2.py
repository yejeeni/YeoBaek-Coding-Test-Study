import itertools

def solution(numbers):    
    numbers = list(numbers)
    perms = []
    prime_numbers = set()
    
    for i in range(1, len(numbers)+1):
        perms.extend(itertools.permutations(numbers, i))
    # print(perms)
    
    for i in perms:
        # '구분자'.join(리스트): 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합침
        num = int(''.join(i))
        
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        
        if is_prime and num > 1:
            prime_numbers.add(num)
    # print(prime_numbers)
    
    return len(prime_numbers)