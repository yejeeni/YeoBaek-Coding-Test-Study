def solution(record):
    names = dict()  #이름, id 저장하는 딕셔너리
    actions = []    #id, 행동 저장하는 리스트

    for r in record:        
        parts = r.split()
        act, uid = parts[0], parts[1]

        if act in ("Enter", "Change"):  #만약 들어오거나 이름이 바뀌는 경우
            #nickname = parts[2]
            names[uid] = parts[2]       #name 딕셔너리에 내용 추가/변경

        if act in ("Enter", "Leave"):   #만약 들어오거나 나오는 경우
            actions.append((act, uid))  #action 딕셔너리에 행동과 id를 순차적 저장
        #print(names, actions)

    answer = []
    for act, uid in actions:       #행동 순서대로
        if act == "Enter":         
            answer.append(f"{names[uid]}님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(f"{names[uid]}님이 나갔습니다.")

    return answer