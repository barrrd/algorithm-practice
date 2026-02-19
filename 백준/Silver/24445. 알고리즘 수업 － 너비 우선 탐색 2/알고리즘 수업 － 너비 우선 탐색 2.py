from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global result
    q = deque()
    q.append(start)
    result[start - 1] = 1
    cnt = 1

    v = set()
    v.add(start)
    while q:
        c = q.popleft()
        for nxt in darr[c]:
            if nxt not in v:
                cnt += 1
                v.add(nxt)
                q.append(nxt)
                result[nxt - 1] = cnt

n, m, k = map(int,input().split())
darr = [[] for _ in range(n + 1)]   # ← 여기만 m+1 → n+1 로 수정
for _ in range(m):
    a, b = map(int,input().split())
    darr[a].append(b)
    darr[b].append(a)

result = [0]*n
for i in range(1, n + 1):
    darr[i].sort(reverse=True)

bfs(k)
for r in result:
    print(r)
