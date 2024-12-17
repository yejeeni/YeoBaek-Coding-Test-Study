s="  TRy HElLo  WORLD " #"TrY HeLlO WoRlD"
def solution(s):
    answer = ''
    s_str = s.split(' ')
    for word_idx in s_str:
        temp = ''
        for i in range(len(word_idx)):
            word = word_idx[i]
            if i % 2 == 0:
                temp += word.upper()
            else:
                temp += word.lower()
        answer += temp +' '
    answer = answer.strip()
    return ''.join(answer)
    #print(answer)
    #return answer
solution(s)