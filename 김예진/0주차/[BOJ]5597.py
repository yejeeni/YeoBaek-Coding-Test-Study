student_list = []
n_student_list = []

for i in range(8):
  number = int(input())
  n_student_list.append(number)

for i in range(1, 11):
  if n_student_list.count(i) == 0:
    student_list.append(i)

print(max(student_list), min(student_list))