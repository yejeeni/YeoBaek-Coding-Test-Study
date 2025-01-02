T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    problem = list(input())
    a = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(problem)-1, -1, -1):
        if problem[i] in a:
            problem.remove(problem[i])
    problem = "".join(problem)
    print('#{0} {1}'.format(test_case, problem))

    # ///////////////////////////////////////////////////////////////////////////////////
