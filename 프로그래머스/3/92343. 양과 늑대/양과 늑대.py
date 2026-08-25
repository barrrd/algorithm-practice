
    
    
    
    
    

def solution(info, edges):
    
    def dfs(v, cand, s, w):
        nonlocal answer
        # 1.break 조건
        if s <= w:
            return

        # 2.갱신
        answer = max(answer, s)
        for nxt in cand:
            if nxt in v:
                continue

            v.add(nxt)
            new_cand = cand[:]
            new_cand.remove(nxt)
            if info[nxt] == 0: # 양
                dfs(v, new_cand + tree[nxt], s + 1, w)
            else:
                dfs(v, new_cand + tree[nxt], s, w + 1)

            v.remove(nxt)
            
    
    
    answer = 0
    
    
    
    
    # 1. init
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        p, c = edge
        tree[p].append(c)
    
    for id, t in enumerate(tree):
        print(f"{id}: {t}")
        
    v = set()
    v.add(0)
    cand = []
    cand.extend(tree[0])
    print(cand)
    dfs(v, cand, 1, 0)
    
    return answer