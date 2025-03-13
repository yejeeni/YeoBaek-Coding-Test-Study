def solution(arr):
    answer = 0

    while True:
        answer += 1
        check = True  # 모든 수가 나누어떨어지는지 확인하는 변수

        for i in arr:
            if answer % i != 0:
                check = False  # 하나라도 나누어떨어지지 않으면 False로 변경
                break  # 더 확인할 필요 없으므로 반복문 탈출
        
        if check:  # 모든 수가 나누어떨어졌다면 반복 종료
            break

    return answer
