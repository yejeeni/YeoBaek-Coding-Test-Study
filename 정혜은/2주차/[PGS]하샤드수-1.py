x=13
def solution(x):
    answer = True

    str_x = str(x)
    sum = 0
    for i in range(len(str_x)):
        sum += int(str_x[i])
    if x % sum != 0:
        answer = False

    return answer
solution(x)