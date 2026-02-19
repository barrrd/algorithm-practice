from collections import deque
# N: 노드 수
# M: 노드 쌍 수
N , M = map(int,input().split())
darr = [list(map(int,input().split())) for _ in range(N-1)]
# want = [list(map(int,input().split())) for _ in range(M)]
# print(darr)
[[2, 1, 2], [4, 3, 2], [1, 4, 3]]

dct = {i: [] for i in range(1,N+1)}
for n1, n2, len in darr:
    dct[n1].append([n2, len])
    dct[n2].append([n1, len])
# print(dct)
# {
# 1: [[2, 2], [4, 3]], 
# 2: [[1, 2]], 
# 3: [[4, 2]], 
# 4: [[3, 2], [1, 3]]
# }

def bfs(u,v):
    q = deque()
    q.append((u, 0))
    vis = set()
    vis.add(u)
    while q:
        x, acc = q.popleft() # x: 노드 번호, acc: 누적 거리
        if x == v:
            return acc
        for nx, w in dct[x]:
            if nx not in vis:
                vis.add(nx)
                q.append((nx, acc + w))
    return 0

for _ in range(M):
    u, v = map(int, input().split())
    print(bfs(u, v))