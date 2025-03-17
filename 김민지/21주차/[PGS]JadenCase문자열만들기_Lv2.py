def solution(s):
    answer = ''
    l = list(s.split(" "))
    a = 0
    for word in l:
        print(word)
        for i in range(len(word)):
            if i == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        if len(l)-1 == a:
            print("break")
            break
        answer += " "
        a += 1

    return answer