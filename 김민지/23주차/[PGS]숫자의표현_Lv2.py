def solution(n):
    answer = 0
    k = 1
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            answer += 1
        k += 1
    return answer

# n = x+(x+1)+(x+2)+...+(x+k−1)  (k개 연속됨)
# n = kx + k(k-1)/2               => while 조건문으로 사용
# kx = n - k(k-1)/2
# x가 자연수 여야함