T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    case = int(input())
    num = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            num1 = num.pop(0) - i
            if num1 <= 0:
                num1 = 0
                num.append(num1)
                break
            else:
                num.append(num1)
        if num[7] == 0:
            break
    print('#{0} {1}'.format(test_case, ' '.join(map(str, num))))
    # ///////////////////////////////////////////////////////////////////////////////////
