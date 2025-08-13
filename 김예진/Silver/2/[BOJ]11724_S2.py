# 방향 없는 그래프가 주어졌을 때 연결요소 구하기
# 각 노드가 어떤 그룹에 속해있는지 저장해야함. 
# 속한 그룹이 있는 노드는 넘어가고, 아직 그룹이 없는 노드라면 그 노드와 연결된 노드를 같은 그룹으로 처리하면서 계산 
# 이 그룹의 수가 연결노드 개수

import collections
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split()) # 정점 수 n, 간선 수 m

graph = [[] for _ in range(n+1)] # 노드 수만큼 그래프 생성
group = [-1] * (n+1) # 각 노드가 어느 그룹에 속해있는지 저장할 배열


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    # 양방향 그래프로 추가
    graph[u].append(v)
    graph[v].append(u)

# node와 연결된 노드를 탐색하는 dfs
def dfs(node):
    for neighbor in graph[node]: # 그래프에서 이 노드와 연결된 이웃 노드
        # 이 이웃노드가 속한 그룹이 없는 경우
        if group[neighbor] == -1:
            group[neighbor] = group[node] # 이 노드, 연결된 노드를 같은 그룹으로 저장

            # 연결된 노드를 기준으로 다시 dfs해서 같은 그룹의 노드 탐색
            dfs(neighbor)

count = 0
for i in range(1, n+1):
    if group[i] == -1: # 그룹 조사 안 한 노드일 경우
        group[i] = i # 본인 번호를 그룹 번호로
        dfs(i) # 연결 노드 탐색
        count += 1 # 탐색하고 dfs를 벗어났으니까 한 그룹의 노드는 탐색이 끝. cnt++

# print(group)
print(count)