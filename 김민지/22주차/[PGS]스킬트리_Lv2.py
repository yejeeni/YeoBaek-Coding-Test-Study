#스킬의 중복은 없음 -> 선행 스킬 순서만 중요한거
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        new_st = "".join([s for s in st if s in skill]) #skill에 있는 값만 new_st에 저장
        print(new_st)
        if skill.startswith(new_st):  #skill이 new_st로 시작한다면 순서대로 맞는거
            answer += 1
        
        #print(st)
        
    return answer

#12345
#12, 1, 123, 1234, 12345