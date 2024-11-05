# 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 1]
# 1, 1/1

# 2]
# 2, 1/2
# 3, 2/1. 분자 증가, 분모 감소

# 3]
# 4, 3/1
# 5, 2/2
# 6, 1/3. 분자 감소, 분모 증가


x = int(input())

line = 1
last = 1

while x > last:
    # 라인 숫자 증가
    line += 1
    # 해당 라인의 마지막 숫자
    last += line

# X가 라인의 몇 번째 인덱스인지
index = last - x

# print("line: %d, last: %d, index: %d"%(line, last, index))

# X가 위치한 줄이 짝수일 경우
if line % 2 == 0:
    분모 = index + 1
    분자 = line - index
else: # X가 위치한 곳이 홀수일 경우
    분모 = line - index
    분자 = index + 1

print("%d/%d"%(분자, 분모))