def solution(begin, target, words):
    
    def dfs(cur, num, v):
        nonlocal answer
        # 1. break
        if cur == target:
            answer = min(answer, num)
            return
        
        # 2. cand 
        # !! 1. zip
        for word in words:
            if word in v:
                continue
            
            count = 0
            for a, b in zip(word, cur):
                if a != b:
                    count += 1
                if count > 1:
                    break
            
            if count == 1:
                v.add(word)
                dfs(word, num + 1, v)
                v.remove(word)
        
    if target not in words:
        answer = 0
        
    else:
        answer = len(words)
        v = set()
        v.add(begin)
        dfs(begin, 0, v)
        
    return answer