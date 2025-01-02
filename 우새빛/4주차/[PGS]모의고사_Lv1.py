def solution(answers):
    answer = []
    
    #수포자 삼인방은 반복적인 패턴으로 찍음 -> 리스트로 작성
    solve_1 = [1, 2, 3, 4, 5] #5개씩 반복
    solve_2 = [2, 1, 2, 3, 2, 4, 2, 5] #8개씩 반복
    solve_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10개씩 반복
    
    #answers리스트와 수포자 삼인방이 찍는 패턴 비교
    check_1 = 0; check_2 = 0; check_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == solve_1[i%5]:
            check_1 += 1
        if answers[i] == solve_2[i%8]:
            check_2 += 1
        if answers[i] == solve_3[i%10]:
            check_3 += 1
    
    #제일 많이 맞춘 사람 answer 리스트에 추가
    max_check = max(check_1, check_2, check_3)
    if check_1 == max_check:
        answer.append(1)
    if check_2 == max_check:
        answer.append(2)
    if check_3 == max_check:
        answer.append(3)
    
    return answer