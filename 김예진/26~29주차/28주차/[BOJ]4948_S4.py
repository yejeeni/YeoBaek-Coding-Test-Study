while True:
    n = int(input())
    if n == 0:
        break
    
    arr = [False, False] + [True] * (2*n - 1) # 0, 1은 false, 2~2n은 true

    for i in range(2, int((n*2)**0.5) + 1):
        if arr[i]: # true이면
            for j in range(i * i, 2 * n + 1, i): # i의 배수들을 전부 False 처리
                arr[j] = False
                # print(arr)

    result = 0
    for i in range(n+1, 2*n+1): # n부터 n의 배수까지
        if arr[i]: # true이면 소수
            result += 1

    print(result)