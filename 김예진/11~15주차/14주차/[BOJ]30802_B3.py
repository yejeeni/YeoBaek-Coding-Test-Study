# 티셔츠는 남아도 되지만 부족하면 안 되고, 펜은 정확히 준비해야 함

n = int(input()) # 참가자 수
size = list(map(int, input().split())) # 티셔츠 사이즈
t, p = map(int, input().split()) # 티셔츠 t장 묶음, 펜 p자루 묶음

shirt = 0
pen = 0

for i in range(len(size)):
  shirt += size[i] // t
  if size[i] % t != 0:
    shirt += 1

print(shirt)

print(n // p, n % p)