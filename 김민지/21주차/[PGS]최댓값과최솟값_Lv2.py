def solution(s):
    answer = ''
    l = list(map(int, s.split(' ')))
    answer = f"{str(min(l))} {str(max(l))}"
    return answer