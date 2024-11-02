n=3
def solution(n):
    answer = 0
    before = 0
    after = 1
    result = 0
    for i in range(n-1):
        result = before + after
        before = after
        after = result
    answer = result % 1234567
    return answer
solution(n)