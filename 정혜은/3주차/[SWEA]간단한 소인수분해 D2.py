T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N = int(input()) # 2,3,5,7,11 a,b,c,d,e
    temp = []
    div = [2,3,5,7,11]
    i = 0
    while i < len(div):
        if N % div[i] == 0:
            temp.append(div[i])
            N = N // div[i]
        else:
            i += 1
    a = temp.count(2)
    b = temp.count(3)
    c = temp.count(5)
    d = temp.count(7)
    e = temp.count(11)
    print('#{0} {1} {2} {3} {4} {5}'.format(test_case, a,b,c,d,e))

    # ///////////////////////////////////////////////////////////////////////////////////
