def F(n): #테스트 7~14 시간초과 및 런타임에러
    if n == 0: #피보나치 수는 F(0) = 0, F(1) = 1일 때,
        return 0
    elif n == 1:
        return 1
    
    return F(n-1) + F(n-2) #F(n) = F(n-1) + F(n-2)

def solution(n):
    return F(n) % 1234567
#->재귀 호출 시 n이 50 이상이면 시간 초과가 나거나 런타임 에러(Python이나 JavaScript 등 일부 언어에서)발생
#  따라서 for 문을 이용하여 해결해볼 것

def solution1(n): #성공
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    Fn1, Fn2 = 0, 1 #초기값
    
    for i in range(2, n+1):
        #temp = Fn2
        #Fn2 = Fn1+Fn2 #F(n) = F(n-1) + F(n-2)
        #Fn1 = temp #F(n-1) 재설정
        
        Fn1, Fn2 = Fn2, Fn1+Fn2
    
    return Fn2 % 1234567

def solution2(n): #힌트보고 개선
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    Fn1, Fn2 = 0, 1 #초기값
    
    for i in range(2, n+1):        
        Fn1, Fn2 = Fn2, (Fn1+Fn2) % 1234567 #매 연산마다 나머지를 구하기
    
    return Fn2
#->n이 매우 큰 경우... n번째 피보나치 수는 언어가 표현할 수 있는 자료형의 범위를 넘어가, 오버플로우 발생
#  [[매 연산마다 %1234567을 적용하여 값이 커지는 것을 방지]]
#  - 불필요한 큰 정수 연산을 피함, 연산 속도가 더 빠름
#  - 메모리 사용량도 줄이기 가능능
#
#<가능한 이유> (a + b) % m = ((a % m) + (b % m)) % m
#             즉, F(n) % m 
#                 = (F(n-1) + F(n-2)) % m
#                 = (F(n-1) % m + F(n-2) % m) % m