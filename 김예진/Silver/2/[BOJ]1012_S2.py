t = int(input())
m, n, k = map(int, input().split())

graph = set() # 배추가 심어진 좌표들의 집합
for i in range(k):
    x, y = map(int, input().split())
    graph.add((x, y))

def dfs_stack(start):
    stack = [start] # DFS를 위한 스택. 시작 노드를 스택에 추가

    while(stack): # 스택이 빌 때까지 끝까지 반복
        node = stack.pop() # 스택에서 (X, Y) 튜플로 된 노드 pop. 여기서 노드는 현재 탐색 중인 배추 좌표
        if node in graph:
            graph.remove(node) # 방문한 노드는 방문 처리
            x, y = node # 노드에서 x, y값 꺼내기

            # 상하좌우 인접 좌표 확인
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy # 인접 좌표 계산
                if (nx, ny) in graph: # 인접 좌표에 아직 방문하지 않은 배추가 있다면
                    stack.append((nx, ny)) # 같은 무리이므로 스택에 추가하여 탐색을 계속

count = 0
while graph:
    start = next(iter(graph))
    dfs_stack(start)
    count += 1

print(count)

"""
# 스택 기반 DFS (깊이 우선 탐색)

# 그래프 정의 (인접 리스트 방식)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs_stack(start):
    visited = set() # 집합
    stack = [start]

    while(stack):
        node = stack.pop() # 스택에서 노드 pop
        if node not in visited: # visied 안에 위에서 pop한 노드가 없는 경우 -> 방문하지 않은 경우
            visited.add(node) # visited에 추가하여 방문을 표시

            # 인접 노드를 뒤에서부터 넣어서 순서 유지
            stack.extend(reversed(graph[node]))
            # 스택은 LIFO이므로 graph = {1 : [2, 3]}의 1번 노드에서 DFS를 시작하면 1->2->3 탐색 순서를 원할텐데, 
            # stack.extend(graph[1]), 즉 stack.extend([2, 3]) 시 스택에 2가 먼저, 3이 나중에 들어가므로 pop()하면 3이 먼저 나와 1->3->2가 됨
            
            # append(x) 시 x를 그 자체로 삽입(ex, x=[1, 2]면 이대로 삽입)
            # extend(x) 시 x는 iterable이어야 하고, itrerable의 요소를 하나씩 꺼내서 list의 맨 끝부분부터 채움

dfs_stack(1)
"""