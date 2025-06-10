# a=1, b=2, ...

r = 31
M = 1234567891

l = int(input())
arr = input()

result = 0

# ord(): 문자를 아스키코드로. chr(): 아스키코드를 문자로
for i in range(len(arr)):
  num = ord(arr[i]) - ord('a') + 1 # 문자의 고유 번호
  result += num * (r ** i)

print(result % M)