# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오. (2 ≤ B ≤ 36)
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

N, B = map(int, input().split())
quotient = 0 # 몫
remainder = 0 # 나머지
result = ''

while(True):
  if N == 0:
    break

  quotient = N // B
  remainder = N % B


# 나머지가 10 이상이라 숫자로 표시할 수 없는 값인 경우
  if remainder > 9:
    # 나머지에서 10을 빼서 A의 유니코드 값을 더한 수를 문자로 변환
    remainder = chr(remainder - 10 + ord('A'))
  # 나머지를 str로 더해줌
  result += str(remainder)

  N = quotient

# 역순으로 출력
print(result[::-1])



# # ======== 다른 풀이 =========

# # 진법의 인덱스
# nums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# N, B = map(int, input().split())
# result=''

# # N이 0이 될 때까지 반복
# while N:
#     # 진법의 인덱스에서 N % B을 인덱스로 하는 값을 추가  
#     result += str(nums[N % B])
#     # N을 B로 나눈 몫으로 저장
#     N //= B

# print(result[::-1])