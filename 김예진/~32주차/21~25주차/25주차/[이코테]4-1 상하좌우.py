"""
1*1 크기의 정사각형으로 나뉜 N*N 크기의 정사각형 공간에 A가 서있다. 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)이다. A는 상하좌우 방향으로 이동 가능하다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있으며, 각각 왼, 오, 위, 아래로 한 칸 이동을 뜻한다. 이때 A가 N*N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
"""

n = int(input())
plans = input().split()
x, y = 1, 1

for plan in plans:
  if plan == 'L':
    if y - 1 >= 1:
      y -= 1

  elif plan == 'R':
    if y + 1 <= n:
      y += 1

  elif plan == 'U':
    if x - 1 >= 1:
      x -= 1

  else:
    if x + 1 <= n:
      x += 1

print(x, y)



# ======== 답안 예시

n = int(input())
plans = input().split()
x, y = 1, 1

# 이동 방향 정의 (L, R, U, D 순서)
dx = [0, 0, -1, 1] # dx, dy 리스트: 방향에 따라 x, y가 얼마나 바뀌는지
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # 명령 문자와 dx, dy의 순서를 일치시킨 리스트

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어나는 경우 무시 (벗어나지 않는 경우에만 이동)
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny

print(x, y)
