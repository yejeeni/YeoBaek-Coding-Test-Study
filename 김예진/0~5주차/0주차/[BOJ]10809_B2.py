s = input()
result = [-1] * 26

for i in range(len(s)):
  a = ord(s[i])
  if result[a - 97] == -1:
    result[a - 97] = s.find(s[i])

for i in result:
  print(i, end=" ")
