T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N = int(input())
    yang = [int(i) for i in input().split()]
    count = 0
    total = 0
    for j in range(len(yang)):
        total += yang[j]
    avg = total / len(yang)
    for x in range(len(yang)):
        if avg >= yang[x]:
            count += 1
    print('#{0} {1}'.format(test_case, count))


    # ///////////////////////////////////////////////////////////////////////////////////
