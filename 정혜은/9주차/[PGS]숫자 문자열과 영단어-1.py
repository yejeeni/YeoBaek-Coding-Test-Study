s="one4seveneight"
def solution(s):
    answer = 0
    temp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in temp:
        if i in temp:
            s = s.replace(i, str((temp.index(i))))
    answer = int(s)
    return answer
solution(s)