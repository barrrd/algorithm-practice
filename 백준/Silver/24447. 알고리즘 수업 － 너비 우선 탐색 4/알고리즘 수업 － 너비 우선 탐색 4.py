from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global depth
    depth[start - 1] = 0
    q = deque()
    count = 1
    q.append((start, 1))
    t = [0]*N
    t[start - 1] = 1
    v = set()
    v.add(start)
    while q:
        c, cnt = q.popleft()
        for nxt in darr[c - 1]:
            if nxt not in v:
                v.add(nxt)
                depth[nxt - 1] = depth[c - 1] + 1
                q.append((nxt, cnt + 1))
                t[nxt - 1] = count + 1
                count += 1
    res = 0
    for i in range(N):
        res +=  t[i] * depth[i]
    return res

######
N, M, R = map(int,input().split())
darr = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int,input().split())
    darr[s - 1].append(e)
    darr[e - 1].append(s)

for d in darr:
    d.sort()
# print(darr)
depth = [-1] * N
vlst = bfs(R)
print(vlst)
# print(depth)
# temp = 0
# for i, res in enumerate(depth, 1):
#     temp += i * res
# print(temp)
