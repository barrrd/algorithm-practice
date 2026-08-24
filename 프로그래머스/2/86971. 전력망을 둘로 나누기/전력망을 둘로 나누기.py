from collections import deque

def find(w, except_num, wires, N):
    # 1. tree 만들기
    tree = {i: [] for i in range(1, N + 1)}
    for i, wire in enumerate(wires):
        if i == except_num:
            continue
        
        w1, w2 = wire
        tree[w1].append(w2)
        tree[w2].append(w1)
        
    # 2. count
    count = 0
    q = deque([(w)])
    v = set()
    v.add(w)
    while q:
        cur_w = q.popleft()
        for nxt in tree[cur_w]:
            if nxt in v:
                continue
            count += 1
            q.append(nxt)
            v.add(nxt)
    
    return count
            


def solution(n, wires):
    answer = float("inf")
    
    for i, wire in enumerate(wires):
        w1, w2 = wire
        
        n1 = find(w1, i, wires, n)
        n2 = find(w2, i, wires, n)
        
        if abs(n1 - n2) < answer:
            answer = abs(n1 - n2)
        
    if answer == float("inf"):
        answer = -1
    
    return answer