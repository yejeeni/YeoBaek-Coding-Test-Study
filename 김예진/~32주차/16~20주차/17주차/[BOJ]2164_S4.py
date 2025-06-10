from collections import deque

n = int(input())
queue = deque(range(1, n+1)) # 1부터 n까지의 큐 생성

while len(queue) > 1:
  queue.popleft() # 가장 위를 제거
  queue.append(queue.popleft()) # 다음 위 카드를 뽑아내서 추가

print(queue[0])


"""
배열을 사용하면?
맨 앞 원소 삭제 시, 나머지 원소를 모두 한 칸씩 앞으로 이동 → O(N)
총 연산 횟수 ≈ N번 반복 → O(N²)

큐를 사용하면?
pop과 push 연산은 O(1)
총 연산 횟수 ≈ N번 → O(N) (훨씬 빠름)

즉, 큐를 사용하면 시간 복잡도가 O(N) 으로 매우 효율적
"""