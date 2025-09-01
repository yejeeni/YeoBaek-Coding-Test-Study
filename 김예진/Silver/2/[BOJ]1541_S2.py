"""
첫째줄에 주어진 식은 0~9. +, -으로만 이루어져있다.
가장 처음과 마지막은 모두 숫자이며, 연속해서 두 개 이상의 연산자가 나타나지 않는다.
5자리보다 많이 연속되는 숫자는 없다
숫자는 0으로 시작할 수 있다.

주어진 식에 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램

=> 마이너스가 나오면 거기 괄호를 추가하는 식
"""

n = input() # 입력받은 문자열 55-50+40

m = n.split('-') # - 를 기준으로 문자열 자르기 55, 50+40
list = []

for i in range(len(m)):
    sum = 0

    k = m[i].split('+') # +를 기준으로 문자열 자르기 50+40 -> 50, 40

    for j in range(len(k)):
        sum += int(k[j]) # 더하기로 연결된 숫자들의 합
    list.append(sum)

total = list[0]
for i in range(1, len(list)):
    total -= list[i]

print(total)