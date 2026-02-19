from collections import deque
def bfs(i,j):
    dir = [(1,0),(0,-1),(-1,0),(0,1)]
    size = 1
    q = deque()
    v.add((i,j))
    q.append([i,j])
    while q:
        ci, cj  = q.popleft()
        for di, dj in dir:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and darr[ni][nj] == 0 and (ni,nj) not in v:
                v.add((ni, nj))
                size += 1
                q.append((ni, nj)) 
    return size

#######################################################
n, m, k = map(int,input().split())
darr = [list(map(int,input().split()))for _ in range(n)]
# print(darr)


v = set()
total_zero = 0
result = []

for i in range(n):
    for j in range(n):
        if darr[i][j] == 0 :
            total_zero += 1
            # print(f'ddd: {total_zero}')
            if (i,j) not in v:
                res = bfs(i,j)
                result.append(res)
                # print(res)
            

[
[1, 1, 1, 0, 0], 
[1, 0, 1, 0, 0], 
[0, 0, 1, 1, 1], 
[1, 1, 0, 0, 0], 
[0, 1, 1, 0, 1]
]

if total_zero == 0:
    print("IMPOSSIBLE")
else:
    need = 0
    for r in result:
        need += (r + k - 1)//k
    if need <= m:
        print("POSSIBLE")
        print(m - need)
    else:
        print("IMPOSSIBLE")