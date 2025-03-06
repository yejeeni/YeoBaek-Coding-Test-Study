def solution(survey, choices):
    answer = ''
    c_list = ["R", "T", "C", "F", "J", "M", "A", "N"]
    char_list= [0, 0, 0, 0, 0, 0, 0, 0]  # R, T, C, F, J, M, A, N
    for i in range(len(survey)):
        if survey[i] == 'RT':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[0] += (4-choices[i])
            elif choices[i] > 4:
                char_list[1] += (choices[i]-4)
        elif survey[i] == 'TR':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[1] += (4-choices[i])
            elif choices[i] > 4:
                char_list[0] += (choices[i]-4)
        elif survey[i] == 'CF':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[2] += (4-choices[i])
            elif choices[i] > 4:
                char_list[3] += (choices[i]-4)
        elif survey[i] == 'FC':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[3] += (4-choices[i])
            elif choices[i] > 4:
                char_list[2] += (choices[i]-4)
        elif survey[i] == 'JM':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[4] += (4-choices[i])
            elif choices[i] > 4:
                char_list[5] += (choices[i]-4)
        elif survey[i] == 'MJ':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[5] += (4-choices[i])
            elif choices[i] > 4:
                char_list[4] += (choices[i]-4)
        elif survey[i] == 'AN':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[6] += (4-choices[i])
            elif choices[i] > 4:
                char_list[7] += (choices[i]-4)
        elif survey[i] == 'NA':
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                char_list[7] += (4-choices[i])
            elif choices[i] > 4:
                char_list[6] += (choices[i]-4)
        
                
    for i in range(4):
        if char_list[i*2] >= char_list[i*2+1]:
            answer += c_list[i*2]
        else:
            answer += c_list[i*2+1]
            
    return answer




"""
def solution(survey, choices):
    from collections import defaultdict

    # 성격 유형별 점수를 저장할 딕셔너리
    score = defaultdict(int)
    types = ["RT", "CF", "JM", "AN"]

    for i in range(len(survey)):
        first, second = survey[i]  # 예: 'RT' -> first='R', second='T'
        choice = choices[i]
        
        if choice < 4:  # 비동의 쪽 선택
            score[first] += 4 - choice
        elif choice > 4:  # 동의 쪽 선택
            score[second] += choice - 4

    # 최종 성격 유형 결정
    answer = ''.join(a if score[a] >= score[b] else b for a, b in types)
    
    return answer
"""