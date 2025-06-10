# 전공평점 구하기
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외


dict = {
  "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, 
  "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

sum = 0
credit_sum = 0
for i in range(20):
  # 과목명, 학점, 등급
  subject, credit, grade = input().split()
  if grade != "P": # 등급이 P가 아닌 경우에만 계산
    credit = float(credit) # input()은 항상 문자열(str)로 입력받기 때문에 형변환
    credit_sum += credit * dict[grade]
    sum += credit

print(credit_sum / sum)