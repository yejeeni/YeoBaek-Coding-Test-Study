def solution(t, p):
    answer = 0
    print(len(t))
    

    for i in range(len(t)-len(p)+1):
        num = t[i:i+len(p)]  # 숫자의 길이만큼 num으로 저장하고
        #print(type(num))
        if num <= p:         #비교
            answer += 1
    return answer

#시간복잡도 O(NxM)  N -> t길이, M -> p길이