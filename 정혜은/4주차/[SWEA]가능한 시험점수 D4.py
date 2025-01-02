T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    problem = int(input())
    score = list(map(int, input().split()))
    count = 0
    result = {0}
    for i in range(len(score)):
        result.update({j + score[i] for j in result})
    count = len(result)
    print('#{0} {1}'.format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////
