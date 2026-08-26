from collections import deque
def solution(n, computers):
    def bfs():
        nonlocal answer
        v = set()
        
        for id in range(n):
            if id in v:
                continue
            
            answer += 1
            v.add(id)
            
            q = deque([id])
            while q:
                cid = q.popleft()
                
                for nid in graph[cid]:
                    if nid not in v:
                        q.append(nid)
                        v.add(nid)
                
            
    
    answer = 0
    # 1. make a graph
    graph = [[] for _ in range(n)]
    for id, com in enumerate(computers):
        for i, c in enumerate(com):
            if id == i:
                continue
            if c == 1:
                graph[id].append(i)
    # for i, g in enumerate(graph):
    #     print(f"{i}: {g}")
        
    bfs()
    return answer