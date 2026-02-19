from collections import deque
def group(i,j):
    dir = [[1,0],[-1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,1],[1,-1]]
    q = deque()
    q.append((i,j))
    res = [[i,j]]
    while q:
        si, sj = q.popleft()
        for di, dj in dir:
            ci, cj = si + di, sj + dj
            if 0 <= ci < h and 0 <= cj < w and (ci, cj) not in vset and darr[ci][cj] == 0.5:
                vset.add((ci,cj))
                q.append((ci,cj))
                res.append([ci,cj])
    return res

###################################
h, w = map(int,input().split())
data = [list(input().rstrip()) for _ in range(h)]
darr = [[0]*w for _ in range(h)]
for i, d in enumerate(data):
    for j, c in enumerate(d):
        darr[i][j] = 1 if c == "." else 0.5

vset = set()
result = None
# ✅ 첫 경계 셀 하나만 찾아서 BFS 1회
for i in range(h):
    if result is not None:
        break
    for j in range(w):
        if darr[i][j] == 0.5:
            vset.add((i,j))       # 시작점 중복 탐색 방지
            result = group(i,j)   # all_points 없이 바로 사용
            break

# 이후 로직은 동일
result.sort()
area = len(result)//2

tdict = {}
for r,c in result:
    tdict.setdefault(r, []).append(c)

for t in tdict.keys():
    tdict[t].sort()
    cols = tdict[t]
    for k in range(0, len(cols)-1, 2):
        area += cols[k+1] - cols[k] - 1

print(area)
