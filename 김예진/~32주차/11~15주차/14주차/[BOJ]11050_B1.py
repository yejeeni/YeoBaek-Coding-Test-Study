def factorial(n):
  if n > 1:
    return n * factorial(n-1)
  else:
    return 1

n, k = map(int, input().split())

print(factorial(n) // (factorial(n - k) * factorial(k)))

# math 라이브러리에 factorial 있음