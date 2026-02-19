from collections import deque
import sys
###########
input = sys.stdin.readline
###########
def bfs(start_r, start_c, r, c, darr):
    dist_arr = [[-1] * c for _ in range(r)] 
    
    dir_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque()
    
    q.append((start_r, start_c))
    dist_arr[start_r][start_c] = 0
    
    max_dist = 0
    
    while q:
        ci, cj = q.popleft()
        cnt = dist_arr[ci][cj] # 현재 거리
        
        if cnt > max_dist:
             max_dist = cnt
        
        for di, dj in dir_list:
            ni, nj = ci + di, cj + dj
            
            if 0 <= ni < r and 0 <= nj < c:
                if darr[ni][nj] == 1 and dist_arr[ni][nj] == -1: 
                    dist_arr[ni][nj] = cnt + 1
                    q.append((ni, nj))
                       
    return max_dist


#############
r, c = map(int, input().split())

darr = [[0] * c for _ in range(r)]
for i in range(r):
    temp = input().strip() 
    for j in range(c):
        if temp[j] == 'L':
            darr[i][j] = 1 # 육지

best_max = -1

# 모든 육지 칸을 시작점으로 하여 BFS 수행
for i in range(r):
    for j in range(c):
        if darr[i][j] == 1: # 육지라면
            # r, c, darr을 인수로 명시적으로 전달
            result = bfs(i, j, r, c, darr)
            if best_max < result:
                best_max = result

print(best_max)

