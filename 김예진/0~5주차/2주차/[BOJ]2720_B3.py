# 동전 개수를 최소로 하여 거스름돈을 주는 프로그램
# 거스름돈은 항상 5.00 이하이고, 동전은 쿼터(0.25), 다임(0.10), 니켈(0.05), 페니(0.01) ((단위: 달러))

# 동전 리스트 (단위: 센트)
coins = [25, 10, 5, 1]

# 테스트 케이스 개수 t
t = int(input())
result = 0

for _ in range(t):
  # 거스름돈 액수 c (단위: 센트. 1달러 = 100센트) (1 <= C <= 500)
  c = int(input())

  # 동전 리스트로 for문 실행
  for coin in coins:
    # 동전 수 계산
    print(c // coin, end = ' ')
    # 남은 거스름돈 계산
    c = c % coin