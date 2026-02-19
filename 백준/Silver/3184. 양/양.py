from collections import deque
# 1. 그룹
def group(i,j):
    global o_count, v_count
    ocnt = 0
    vcnt = 0
    if darr[i][j] == 1:
        ocnt = 1
    elif darr[i][j] == 2:
        vcnt = 1    
    q = deque()
    q.append((i,j))
    # tmp = [[i,j]]
    while q:
        ci , cj = q.popleft()
        for di, dj in dir:
            ni, nj = di + ci, dj + cj
            if 0 <= ni < R and 0 <= nj < C and (ni,nj) not in g and darr[ni][nj] != -1:
                if darr[ni][nj] == 1:
                    ocnt += 1
                elif darr[ni][nj] == 2:
                    vcnt += 1
                g.add((ni, nj))
                q.append((ni, nj))
                # tmp.append([ni, nj])
    if ocnt > vcnt:
        o_count += ocnt
    elif ocnt <= vcnt:
        v_count += vcnt
    
    # return tmp if ocnt + vcnt > 0 else None
################################################# 
# #: 울타리(-1), .: 빈곳(), o: 양(1), v: 늑대(2)
R, C = map(int,input().split())
darr = [[] for _ in range(R)]
for i in range(R):
    tmp = list(input())
    for t in tmp:
        if t == "#": # 울타리
            darr[i].append(-1)
        elif t == ".": # 빈 곳
            darr[i].append(0)
        elif t == "o": # 양
            darr[i].append(1)
        elif t == "v": # 늑대
            darr[i].append(2)

# [1]. 같은 영역 위치 찾기 != -1
g = set()
dir = [[1,0],[0,1],[-1,0],[0,-1]]
glst = []
o_count = 0
v_count = 0

for i in range(R):
    for j in range(C):
        if (i,j) not in g and darr[i][j] != -1:
            g.add((i,j))
            group(i,j)
            # res = group(i,j)
            # if res != None:
            #     glst.append(res) # group 위치 만
# print(glst)
print(o_count, v_count)
