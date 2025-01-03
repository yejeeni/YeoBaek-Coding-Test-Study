# MN개 단위로 나뉜 M*N 크기의 보드를 잘라 8*8 크기의 체스판으로
# 각 칸은 검/흰 중 하나로 칠해져있음. 체스판은 맨 왼쪽 위칸이 흰색이거나 검은색이거나임
# 아무데서나 8*8 크기로 자를 수 있음. 다시 칠해야하는 정사각형의 최수 개수 구하기

# W(0, 0) | B(0, 1) | W(0, 2) | B(0, 3)
# B(1, 0) | W(1, 1) | B(1, 2) | W(1, 3)
# -> (0, 0)이 W일 때, 좌표합이 짝수인 곳은 W, 홀수인 곳은 B임
#    (0, 0)이 B일 때, 좌표합이 짝수인 곳은 B, 홀수인 곳은 W임
#    

n, m = map(int, input().split())
board = []
for i in range(n):    
	board.append(input())
result = []

# 보드 내에서 체스판 크기 8*8를 맞추도록 지정
for i in range(n-7):
  for j in range(m-7):
    white = 0
    black = 0
    # 체스판 크기 8*8만큼
    for a in range(i, i+8):
        for b in range(j, j+8):
            if (a + b) % 2 == 0: # 좌표합이 짝수일 경우,
                # 시작이 W일 때, 짝수는 W, 홀수는 B -> W가 아닐 때를 카운트 
                # 시작이 B일 때, 짝수는 B, 홀수는 W -> B가 아닐 때를 카운트
                asdf = board[a][b]
                if board[a][b] != 'W':
                    white += 1
                if board[a][b] != 'B':
                    black += 1
            else: # 좌표합이 홀수일 경우
                asdf = board[a][b]
                # 시작이 W일 때, 홀수가 B가 아닐 때를 카운트
                if board[a][b] != 'B':
                    white += 1
                # 시작이 B일 때, 홀수가 W가 아닐 때를 카운트
                if board[a][b] != 'W':
                    black += 1

    result.append(white)
    result.append(black)

print(min(result))