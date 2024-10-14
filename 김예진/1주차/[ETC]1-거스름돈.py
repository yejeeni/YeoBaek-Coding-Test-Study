coin = [500, 100, 50, 10]
pay = int(input())
result= 0

for i in coin:
  result += pay // i
  
  pay %= i


print(result)