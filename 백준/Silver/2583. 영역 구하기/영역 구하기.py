from collections import deque
def bfs(i,j):
    dir = [[1,0 ], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append((i,j))
    tlst = 1
    while q:
        si ,sj = q.popleft()
        for di, dj in dir:
            ci, cj = si + di, sj + dj
            if 0 <= ci< M and 0 <= cj< N and (ci, cj) not in vset and arr[ci][cj] == 0:
                vset.add((ci, cj))
                q.append((ci, cj))
                tlst += 1
    return tlst

##################3
# [1] 입력 M: 세로, N: 가로, K: 직사각형 수
M, N, K  = map(int,input().split())
datas = [list(map(int,input().split()))for _ in range(K)]
arr = [[0]*N for _ in range(M)]

for data in datas:
    sj, si, ej, ei = data # 0 2 4 4
    csi, csj = M - si - 1 , sj
    cei, cej = M - ei, ej - 1
    for row in range(cei, csi +1):
        for col in range(csj, cej+1):
            arr[row][col] = 1

cnt = 0
result = []
vset = set()
for i in range(M):
    for j in range(N):
        if (i,j) not in vset and arr[i][j] == 0:
            vset.add((i,j))
            result.append(bfs(i,j))
print(len(result))
result.sort()
print(*result)
