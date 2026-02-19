# 0. 초기 설정
case = int(input())
# print(case)

# 1. dfs
def dfs (start):
    global graph, visited, n, k, data
    visited[start] = True
    
    # deep
    for next in range(0,n): # col
        if not visited[next] and graph[start][next]:
            dfs(next)
    return 
    

for _ in range(case):
    datas = list(map(int,input().split()))

    # 기본 변수
    n = datas[0]
    k = datas[1]
    data = datas[2:]
    
    # graph 생성
    graph = [[False]*(n) for _ in range(n)]
    for i in range(0,len(data),2):
        graph[data[i]][data[i+1]] = True
        graph[data[i+1]][data[i]] = True
    
    # visited 생성
    visited = [False]*n
    
    #
    dfs(0)
    if visited == [True]*n:
        print('Connected.')
    else:
        print('Not connected.')
    
    