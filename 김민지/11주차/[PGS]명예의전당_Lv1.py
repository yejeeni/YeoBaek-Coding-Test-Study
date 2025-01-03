def solution(k, score):
    answer = []
    k_list = []

    for s in score:
        if len(k_list) < k:
            k_list.append(s)
        elif len(k_list) >= k:
            if s > k_list[0]:
                k_list[0] = s
        k_list.sort()

        answer.append(min(k_list))
    return answer