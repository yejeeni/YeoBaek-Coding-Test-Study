a = []
max_num = -1
max_row = 0
max_col = 0

for i in range(9):
  num = list(map(int, input().split()))
  a.append(num)
  input_max = max(num)
  
  if input_max > max_num:
    max_num = input_max
    max_row = i+1
    max_col = num.index(input_max) + 1

print(max_num)
print(max_row, max_col)