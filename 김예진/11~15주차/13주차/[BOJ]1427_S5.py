n = int(input())

n_arr = list(map(int, str(n)))
n_arr.sort(reverse=True)

for i in n_arr:
  print(i, end='')