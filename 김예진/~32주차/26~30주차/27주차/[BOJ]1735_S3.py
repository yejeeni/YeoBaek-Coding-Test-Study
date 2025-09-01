# 첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 
# 첫째 줄에 입력반은 분수의 합의 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.

import math

at, ab = map(int, input().split())
bt, bb = map(int, input().split())

rt = at * bb + ab * bt
rb = ab * bb

rgcd = math.gcd(rt, rb)
print(rt // rgcd, rb // rgcd)