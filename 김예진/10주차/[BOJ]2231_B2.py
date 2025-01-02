n = int(input())

for i in range(1, n+1):
  n_list = list(map(int, str(i))) # 숫자 각 자리 별 분리
  n_sum = sum(n_list) + i # 숫자와 해당 숫자의 자리수를 더하여 분해합 계산

  if n_sum == n: # 계산한 분해합이 n과 일치하는 경우
    print(i) # i가 가장 작은 생성자
    break

  if i == n: # 반복문이 n만큼 반복되었으면 분해합이 없음
    print(0)