# 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither

while True:
  a, b = map(int, input().split())

  if a == 0 & b == 0:
    break
  elif b % a == 0:
    print("factor")
  elif a % b == 0:
    print("multiple")
  else:
    print("neither")