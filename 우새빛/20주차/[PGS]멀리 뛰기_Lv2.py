from itertools import permutations

def solution(n): #테스트 3~16 시간초과
    answer = 0
    
    # 4 -> (1, 1, 1, 1) 2가 0개 0 <= 4
    #      (2, 1, 1)        1개 1 <= 4
    #      (2, 2)           2개 2 <= 4
    
    max_of_2 = n//2
    
    for i in range(max_of_2+1):
        num_list = [2]*i + [1]*(n-2*i) #가능한 칸 나열(순서 따지지 않고)
        
        #print(num_list) / 	[1, 1, 1, 1], [2, 1, 1], [2, 2]
        
        answer += len(set(permutations(num_list, len(num_list)))) #가능한 순열 나열(단, 중복은 피함) 
        #print(set(permutations(num_list, len(num_list)))) /
        #{(1, 1, 1, 1)} {(1, 2, 1), (2, 1, 1), (1, 1, 2)} {(2, 2)}
        
    return answer % 1234567
#->순열을 각각 다 구하는 것이 시간이 너무 오래 걸리는 것으로 판단단

import math

def solution1(n): #성공
    answer = 0
    
    max_of_2 = n//2 #2가 최대 몇개 들어갈 수 있는지
    
    for i in range(max_of_2+1):
        #print(list(combinations(range(n-i), i))) / [()] [(0,), (1,), (2,)] [(0, 1)] -> len 적용
        #print(math.comb(n-i, i)) / 1 3 1
        
        answer += math.comb(n-i, i) #전체에서 2가 몇번째에 있을지 조합으로 구하기
        
    return answer % 1234567



#<매 연산마다 % 1234567이 가능한가...?>
#피보나치 수 : 가능   -> F(n) = (F(n-1) + F(n-2))를 % 1234567하여도 점화식 구조가 유지
#멀리 뛰기   : 불가능 -> comb(n, r) = n! / (r! * (n-r)!)은 팩토리얼 기반 연산...
#                                                         따라서, 중간 과정에서 %를 적용하면 정보가 손실될 수 있음