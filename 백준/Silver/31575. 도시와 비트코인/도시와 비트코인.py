# dfs
def dfs(t_row,t_col):
    global temp
    global visited

    visited[t_row][t_col] = True

    if t_row == row  and t_col == col: # dfs 재귀에서 맞은 경우!
        temp = 1
        return 1
    if t_row +1 < row+1 and graph[t_row+1][t_col] and not visited[t_row+1][t_col]:
        dfs(t_row+1,t_col)
        if temp == 1:
            return 1
    if t_col +1 < col + 1 and graph[t_row][t_col+1] and not visited[t_row][t_col+1]:
        dfs(t_row,t_col+1)
        if temp == 1:
            return 1
    return temp

# 1. 입력 5,4
col, row = list(map(int,input().split()))
datas = [list(map(int,input().split())) for _ in range(row)]
# print(datas)

# 2. graph & vistied
graph = [[False] * (col+1) for _ in range(row+1)]
for i in range(row):
    for j in range(col):
        if datas[i][j] == 1:
            graph[i+1][j+1] = True

visited = [[False] * (col+1) for _ in range(row+1)]

# print(graph) 

# 3. 실행
temp = 0
result = dfs(1,1)
# print(result)
if result == 1:
    print('Yes')
else:
    print('No')