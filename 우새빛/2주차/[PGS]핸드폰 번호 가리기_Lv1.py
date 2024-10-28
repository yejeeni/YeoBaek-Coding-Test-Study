def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += '*'
        else:
            answer += str(phone_number[i])
            
    return answer

def solution2(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]
            #문자열 연산과 슬라이싱을 이용하여 코드 더 짧게 가능

print("결과1 : " + solution('01033334444'))
print("결과2 : " + solution2('01033334444'))

#결과1 : *******4444
#결과2 : *******4444