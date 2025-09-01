from collections import defaultdict, deque

# 정점의 개수 n, 간선의 개수 m, 탐색을 시작할 정점의 번호 v
n, m, v = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2) # 양방향 그래프로 간선 추가
    graph[n2].append(n1)

# 노드 번호가 작은 순으로 탐색하기 위해 노드 정렬
for node in graph:
    graph[node].sort()

# DFS 스택 기반 (LIFO)
def dfs(graph, start):
    visited = set() # 방문한 노드 저장용 집합
    stack = [start] # DFS 탐색을 위한 스택
    result = [] # 방문 순서 기록용 리스트

    while stack:
        node = stack.pop() # 스택에서 노드 하나 꺼내기
        if node not in visited: # 방문 기록이 없는 노드인 경우
            visited.add(node) # 방문 list에 추가
            result.append(node) # 방문 순서 기록
            # 인접노드를 역순으로 넣어서 번호가 작은 것부터 pop되도록 유지
            stack.extend(reversed(graph[node]))
    return result

# BFS 큐 기반 (FIFO)
def bfs(graph, start):
    visited = set() # 방문 노드 집합
    queue = deque([start]) # 시작 노드를 큐에 추가
    result = [] # 방문 순서 기록용 리스트

    while queue:
        node = queue.popleft() # 큐의 맨 앞에서 노드를 꺼냄
        if node not in visited: # 아직 방문하지 않은 경우
            visited.add(node) # 방문 처리
            result.append(node) # 방문 순서 기록
            queue.extend(graph[node]) # 인접노드를 큐의 뒤에 추가

    return result

dfs_result = dfs(graph, v)
bfs_result = bfs(graph, v)

print(*dfs_result)
print(*bfs_result)