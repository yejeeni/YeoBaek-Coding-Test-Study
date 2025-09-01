"""
 버블정렬, 선택정렬 같은 것으로 풀어도 시간복잡도가 O(n^2)이라 시간초과
 퀵정렬 같은 것으로 풀어도 O(nlong)이라 시간초과나 메모리 부족이 생길 듯
 -> O(n+데이터의 최대값 k)의 시간복잡도를 가지는 계수정렬(Counting Sort)을 사용해야 함
    최대값이 작을 수록 유리
 """

import sys

n = int(input())
count = [0] * 10001 # 계수정렬에 이용할 리스트

for i in range(n):
  num = int(sys.stdin.readline())
  count[num] += 1 
  # count 리스트는 인덱스에 해당하는 값이 몇 번 들어왔는지 저장함
  # 그러므로 입력받은 num을 인덱스로 하는 위치의 값을 1 증가

for i in range(1, 10001):
  if count[i] != 0:
    for j in range(count[i]):
      print(i)