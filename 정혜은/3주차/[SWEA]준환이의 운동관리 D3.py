T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    # L, U, X
    L, U, X = map(int, input().split())
    if X < L:
        print('#{0} {1}'.format(test_case, L-X))
    elif L < X < U:
        print('#{0} {1}'.format(test_case, 0))
    elif X > U:
        print('#{0} {1}'.format(test_case, -1))

    # ///////////////////////////////////////////////////////////////////////////////////
