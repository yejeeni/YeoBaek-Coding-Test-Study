def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])


    answer = sorted(list(set(answer)))

    return answer

#평균적인 경우: O(N^2)
#최악의 경우: O(N^2 log N)