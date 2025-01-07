# 가로 세로 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있고,
# 이 도화지 위에 10 X 10 색종이를 색종이의 변과 도화지의 변이 평행하게 붙임
# 색종이가 붙은 영역의 넓이 구하기 
# -> 도화지가 올라간 곳이 어딘지만 체크해두면 됨

# 색종이의 수
n = int(input())
# 도화지 초기화
paper =  [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
  # 좌측 하단의 좌표
  x, y = map(int, input().split())
  # 10 X 10 색종이 영역은 1로 저장
  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j] = 1

result = 0
for i in paper:
  result += sum(i)

print(result)
