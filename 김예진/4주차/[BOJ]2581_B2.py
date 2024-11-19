# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다

m = int(input())
n = int(input())
arr = []

# m부터 n까지 반복
for i in range(m, n+1):
  is_prime = True
  if i < 2:
    continue # 2보다 작은 수는 소수가 아니므로 건너뜀

  # 2부터 숫자-1까지 반복
  # for j in range(2, int(i**0.5) + 1):  # 더 나은 코드. i의 제곱근까지만 확인해도 된다. 모든 수는 그 제곱근을 기준으로 대칭적으로 약수가 존재하기 떄문
  for j in range(2, i):
    # 숫자를 나눴을 때 나눠떨어지면 소수가 아님
    if i % j == 0:
      is_prime = False
      break

  if is_prime:
    arr.append(i)

if len(arr) > 0:
  print(sum(arr))
  print(min(arr))
else:
  
  print(-1)