# 최소힙 구현
import sys
import heapq # 힙 구현 모듈

n = int(sys.stdin.readline()) # 연산 개수

heap = [] # 최소 힙으로 사용할 리스트

for _ in range(n):
    x = int(sys.stdin.readline()) # 연산 정보

    if x == 0:
        if heap:
            # 배열에서 가장 작은 값을 뽑아내서 출력
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        # 자연수 x를 배열(힙)에 추가
        heapq.heappush(heap, x)
        