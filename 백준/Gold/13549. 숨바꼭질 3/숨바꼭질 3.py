from collections import deque
N, K = map(int,input().split())
dir = [-1, 1]
max_length = 100001

vset = set()
q = deque()
q.append((N,0))
while q:
    x, time = q.popleft()
    if x == K:
        # print()
        print(time)
        break
    d = 2
    if x*d not in vset and x*d < max_length:
        vset.add(x*d)
        q.append((x*d, time)) 
    for m in dir:
        if (x + m) not in vset and (x + m) < max_length:
            # print(x+m)
            vset.add(x + m)
            q.append((x+m, time + 1)) 