"""
원형 테이블에 앉은 N명의 사람 중 K번째 사람을 제거하는 과정을 모두 제거될 때까지 반복
ex, (N, K) = (7, 3)이면  <3, 6, 2, 7, 5, 1, 4>
"""

from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n + 1))
result = []

while queue:
  # deque.rotate(n): n이 음수면 왼쪽으로, 양수면 오른쪽으로 n만큼 큐를 회전
  queue.rotate(-(k-1))
  result.append(queue.popleft())

# "구분자".join(리스트): 문자열로 변환할 리스트의 각 요소 사이에 구분자를 넣어 하나의 문자열로 만듦
print("<" + ", ".join(map(str, result)) + ">")