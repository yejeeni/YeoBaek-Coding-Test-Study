def solution(elements):
    n = len(elements)
    elements = elements * 2  # 원형 처리를 위해 2배 확장
    sum_set = set()

    for l in range(1, n + 1):  # 부분 수열 길이 1부터 n까지
        for s in range(n):  # 시작 인덱스는 원래 길이까지만
            sub_sum = sum(elements[s:s + l])
            sum_set.add(sub_sum)
            
    answer = len(sum_set)

    return answer