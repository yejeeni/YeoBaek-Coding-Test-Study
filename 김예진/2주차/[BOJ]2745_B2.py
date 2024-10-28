# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

N, B = input().split()
lenght = len(N)
B = int(B)
result = 0

for i in range(lenght):
  num = N[i]
  if 'A' <= num <= 'Z':
    result += (ord(num) - ord('A') + 10) * (B**(lenght - i - 1))
  else:
    result += int(num) * B**(lenght - i - 1)

print(result)

# 내장함수 쓰는 풀이
# N, B = input().split()
# print(int(n,int(b)))