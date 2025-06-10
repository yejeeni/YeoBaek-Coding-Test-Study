"""
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 큐의 맨 뒤에 재배치
"""

from collections import deque

num = int(input())

for _ in range(num):
  n, m = map(int, input().split()) # 문서의 개수 n, 몇 번째로 인쇄됐는지 궁금한 문서 번호(인덱스 0부터 시작)
  priority = list(map(int, input().split())) # 문서들 우선순위

  queue = deque((priority[i], i) for i in range(n)) # 큐(우선순위, 인덱스)
  count = 0

  while queue:
    if queue[0][0] < max(queue, key = lambda x: x[0])[0]: # 우선순위만 비교
      queue.append(queue.popleft())
    else:
      count += 1
      document = queue.popleft() 

      if document[1] == m:
        print(count)
        break