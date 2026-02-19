import sys
from collections import deque

input = sys.stdin.readline
def bfs(start):
    global v, order, cnt
    q = deque()
    q.append(start)
    v[start] = True
    while q:
        c = q.popleft()
        order[c] = cnt
        cnt += 1
        for n in darr[c]:
            if not v[n]:
                v[n] = True
                q.append(n)


n, m, r = map(int,input().split())
darr = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int,input().split())
    darr[s].append(e)
    darr[e].append(s)
# print(darr)
# arr = list(sorted(darr, key = lambda x,x))

for i in range(1,n+1):
    darr[i].sort()
# print(darr)

v = [False]*(n+1)
order = [0]*(n+1)
cnt = 1

bfs(r)

for i in range(1, n+1):
    print(order[i])