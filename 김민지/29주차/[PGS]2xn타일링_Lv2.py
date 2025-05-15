def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    n1, n2 = 1, 2
    for i in range(3, n+1):
        n1, n2 = n2, (n1 + n2) % 1000000007 

    return n2

# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8
# 6 -> 13
# 7 -> 21    => 피보나치