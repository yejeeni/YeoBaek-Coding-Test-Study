"""
그래프
각 컴퓨터는 노드(node), 컴퓨터 간 연결은 간선(edge)
graph = [[] for _ in range(n+1)] 부분은 인접 리스트 방식으로 그래프를 표현한 것이고, 양방향 연결이기 때문에 graph[a].append(b) 와 graph[b].append(a) 를 모두 수행

깊이 우선 탐색(DPS)
재귀 함수로 구현한 DFS 방식
def dfs(u) 함수가 탐색을 통해 방문한 컴퓨터는 infected 배열에 기록하여 방문 여부를 확인
"""

n = int(input()) # 컴퓨터의 수 (100 이하인 양의 정수, 1번부터 인덱싱)
m = int(input()) # 네트워크상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [ [] for _ in range(n+1) ] # arr[컴퓨터번호][[연결된 컴퓨터]]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향으로 연결돼있어서 두군데 모두 저장

infected = [0] * (n+1) # 컴퓨터 수만큼의 0 배열을 만들고, 감염은 1로 표시할 것
infected[1] = 1

def dfs(u):
    for v in graph[u]:
        if infected[v] == 0:
            infected[v] = 1
            dfs(v)

dfs(1)

print(sum(infected)-1)