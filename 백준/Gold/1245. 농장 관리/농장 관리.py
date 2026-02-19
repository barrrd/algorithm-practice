from collections import deque
#####
def group (i,j): # group 좌표
    q = deque()
    q.append((i,j))
    # tlst = []
    # tlst.append((i,j))

    h = arr[i][j]
    is_peak = True
    while q:
        ci, cj = q.popleft()
        for di ,dj in dir:
            si, sj = ci + di, cj + dj
            if 0 <= si < N and 0 <= sj < M:
                # 1.하나라도 그 이상이면 피크 아님
                if arr[si][sj] > h: 
                    is_peak = False
                # 2. 높이 동일 & not 방문
                elif arr[si][sj] == h and (si, sj) not in g:     
                    q.append((si, sj))
                    g.add((si, sj))
                #     tlst.append([si,sj])
    return is_peak

# N: row, M: col
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)

dir =[(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
# dir = [(1,0), (-1,0), (0,1), (0,-1)]

# [1] group들 좌표
g = set()
glst = []
ans = 0

for i in range(N):
    for j in range(M):
        if (i,j) not in g and arr[i][j] != 0:
            # print(i,j)
            # print()
            g.add((i,j))
            is_peak = group(i, j)
            # glst.append(plateau)
            if is_peak:
                ans += 1
            # glst.append(group(i,j))
print(ans)