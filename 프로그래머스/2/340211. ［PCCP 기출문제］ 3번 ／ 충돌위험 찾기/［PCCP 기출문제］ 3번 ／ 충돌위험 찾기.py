from collections import Counter
def solution(points, routes):
    # 1)
    pos = {idx: tuple(rc) for idx, rc in enumerate(points,start = 1)}
    active = set(idx for idx in range(1, len(routes) + 1 ))
    prog = {id: 0 for id in active}
    locate = {idx: pos[ids[0]] for idx, ids in enumerate(routes, start = 1 )}
    answer = 0
    # print(pos)
    # print(active)
    # print(prog)
    # print(locate)
    # 2)
    def move(start, target):
        cr, cc = start
        tr, tc = target
        if cr != tr:
            if cr < tr: cr += 1
            else: cr -= 1
        elif cc != tc:
            if cc < tc: cc += 1
            else: cc -= 1
            
        return cr, cc
    
    # 3) 
    cnt = Counter(locate[id] for id in active)
    answer += sum(1 for v in cnt.values() if v >= 2)
    ## 1. execute
    while active:
        fin = []
        for id in active:
            ### 1. init
            path = routes[id - 1]
            j = prog[id] + 1
            target = pos[path[j]]
            ### 2. update
            locate[id] = move(locate[id], target)
            ### 3. add the remove id list: check that it is reach the target
            if locate[id] == target:
                prog[id] += 1
                if prog[id] == len(path) - 1:
                    fin.append(id)
        ## 2. check the locate and count 
        cnt = Counter(locate[id] for id in active)
        answer += sum(1 for v in cnt.values() if v >= 2)
        ## 3. remove the fin
        for f in fin:
            active.remove(f)
            
    return answer