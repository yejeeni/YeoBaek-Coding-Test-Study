# 2보다 큰 짝수 N이 주어졌을 때, N은 두 소수의 합으로 나타낼 수 있다.
# 골드바흐 파티션의 수 구하기 (중복 제거)

t = int(input())

for _ in range(t):
    n = int(input())

    arr = [False, False] + [True] * (n-1)

    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    cnt = 0
    for i in range(2, n//2 + 1): # 2부터 반절까지만 보면 됨 (중복 제거 겸)
        if arr[i] and arr[n-i]:
            cnt += 1
        """
        n=6, arr = [F, F, T, T, F, T, F]일 때
             index  0  1  2  3  4  5  6
        
        i번 원소가 true이고 (=소수), n-i번 원소가 true이면
    ex, 3                          6-3=3    
        골드바흐 파티션이 되는 것
        인덱스가 곧 숟자라서 가능!
        """
        
    print(cnt)