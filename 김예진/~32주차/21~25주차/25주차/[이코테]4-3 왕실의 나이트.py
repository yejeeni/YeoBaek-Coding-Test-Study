"""
8*8 좌표 평면의 정원의 특정 한 칸에 나이트가 서있다. 정원에서 행 위치를 표현할 때는 1부터 8로, 열 위치를 표현할 때는 a부터 h로 표현한다.
나이트가 이동할 때는 L자 형태로만 이동할 수 있으며, 정원 밖으로는 나갈 수 없다. 나이트는 특정 위치에서 다음 두 가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력
"""

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 방향
move_types = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
arr = []
for move in move_types:
  next_row = row + move[0]
  next_col = col + move[1]

  if 1 <= next_row <= 8 and 1 <= next_col <= 8:
    count += 1
    # coord =  str(chr(int(ord('a')) + next_col - 1)) + str(next_row)
    # arr.append(coord)

print(count)
# for a in arr:
#   print(a)