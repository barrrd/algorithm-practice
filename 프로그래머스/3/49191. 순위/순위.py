from collections import deque

def solution(n, results):
    answer = 0
    
    lst = [[] for _ in range(n + 1)]
    
    # 1. lst
    for win, lose in results:

        lst[win].append(lose)
    print(lst)
    
    # 2. connect indirect
    for id in range(1, n + 1):
                
        q = deque([id])
        v = set()
        while q:
            cid = q.popleft()
            
            for lose in lst[cid]:
                if lose in v:
                    continue
                
                v.add(lose)
                q.append(lose)
        # 3. update
        lst[id] = v
        
    # 4.answer
    for id in range(1, n + 1):
        win_count = len(lst[id])
        lose_count = 0
        
        for other in range(1, n + 1):
            if id in lst[other]:
                lose_count += 1
        
        if win_count + lose_count == n - 1:
            answer += 1
                
                
                
    
    
    return answer