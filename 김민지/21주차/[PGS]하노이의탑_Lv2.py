def hanoi(n, s, m, e, answer):
    if n == 1:
        answer.append([s, e])
        return
    hanoi(n - 1, s, e, m, answer)  # n-1개를 보조 기둥으로 이동
    answer.append([s, e])
    hanoi(n - 1, m, s, e, answer)  # n-1개를 목표(end) 기둥으로 이동
    
def solution(n):
    #짝수개 3, 홀수개 2
    answer = []
    hanoi(n, 1, 2, 3, answer)  # start(시작), middle, end(목표)

    return answer