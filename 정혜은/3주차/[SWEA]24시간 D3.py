T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    before, after = map(int, input().split())
    result = before + after
    if result > 24:
        result -= 24
        print('#{0} {1}'.format(test_case, result))
    elif result == 24:
        print('#{0} {1}'.format(test_case, 0))
    else:
        print('#{0} {1}'.format(test_case, result))

    # ///////////////////////////////////////////////////////////////////////////////////
