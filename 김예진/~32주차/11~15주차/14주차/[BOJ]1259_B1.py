# 거꾸로 읽어도 똑같은 수인지

while True:
  n = input()
  if n == '0':
    break

  is_palindrome = True

  for i in range((len(n)//2)):
    if n[i] == n[len(n)-i-1]:
      continue
    else:
      is_palindrome = False
  
  if is_palindrome:
    print('yes')
  else:
    print('no')
  
  """
  # 훨씬 간단한 코드
   if n == n[::-1]: # 슬라이싱을 통해 문자열을 뒤집어서 일치하는지 검사하면 됨
        print('yes')
    else:
        print('no')
  """