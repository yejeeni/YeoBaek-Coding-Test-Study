import re
def solution(new_id):
    answer = new_id
    
    #1단계. 소문자로 치환
    answer = answer.lower()
    
    #2단계. 특수문자 제거
    answer = re.sub(r'[^a-z0-9._-]', '', answer)

    #3단계. 마침표의 연속 제거
    answer = re.sub(r'\.+', '.', answer)

    #4단계. 처음 끝의 마침표 제거
    if answer.startswith('.'):
        answer = answer[1:]

    if answer.endswith('.'):
        answer = answer[:-1]

    #5단계. 빈 문자열이면 new_id에 a대입
    if answer == "":
        answer = "a"
    
    #6단계. 15자 이하이게
    if len(answer) > 15:
        answer = answer[:15]
    if answer.endswith('.'):
        answer = answer[:-1]
    
    #7단계. 3자 이상이게
    done = True
    if len(answer) < 3:
        while done:
            answer += answer[len(answer)-1]
            if len(answer) >= 3:
                done = False

    return answer




"""
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""