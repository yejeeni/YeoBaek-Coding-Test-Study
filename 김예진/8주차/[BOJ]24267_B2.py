n = int(input())

# i는 1부터 n-2까지       n-2 번
#   j는 i+1 부터 n-1까지  n-1-i 번
#     k는 j+1부터 n까지   n-j 번

print((n * (n-1) * (n-2))//6)
print(3)