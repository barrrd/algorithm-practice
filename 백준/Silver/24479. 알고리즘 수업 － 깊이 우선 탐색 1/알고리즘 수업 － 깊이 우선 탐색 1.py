import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(start):
    global result, visited, order
    result[start - 1] = order
    order += 1
    nlst  = darr[start - 1]
    for nxt in nlst:
        if not visited[nxt - 1]: 
            visited[nxt - 1]  =  True
            dfs(nxt)
            # visited[nxt - 1]  =  False


    
##############
"""
K에서 시작해서 dfs로 노드 방문 순서라고 함

"""
N, M, K = map(int,input().split())

darr = [[] for _ in range(N)]
# 1. darr 저장
for _ in range(M):
    s, e = map(int,input().split())
    darr[s - 1].append(e)
    darr[e - 1].append(s)
# 2. 오름차순으로 
for d in darr:
    d.sort()
# print(darr)

result = [0]*N
# result[K - 1] = 1
visited = [False]*N
visited[K -1] = True
order = 1
dfs(K)

for r in result:
    print(r)