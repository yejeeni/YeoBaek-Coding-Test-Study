"""
최대힙: 최소힙에서, 값을 음수로 저장하는 방식을 이용해서 구현
"""

import sys
import heapq

n = int(sys.stdin.readline()) # 연산 개수
heap = [] # 최대 힙으로 사용할 리스트

for _ in range(n):
    x = int(sys.stdin.readline()) # 연산 정보
    
    if x == 0:
        if heap:
            # 배열에서 가장 큰 값을 출력하고 배열에서 제거
            print(-heapq.heappop(heap)) # 앞에 마이너스를 달아서 음수를 양수로 변환
        else:
            print(0)
    else:
        # 자연수 x를 힙에 추가하는데, 양수를 음수로 바꿔서 추가하여 최대힙으로 구현
        heapq.heappush(heap, -x)
