from collections import deque
def bfs(r):
    cset = set()
    q = deque()
    q.append(r)
    cset.add(r)
    while q: 
        k = q.popleft()
        # print(k)
        # print(p_c[k])
        for child in p_c[k]:
            if child not in cset:
                # print(child)
                cset.add(child)
                q.append(child)
                # print(cset)
                # print(q)
    return cset

N = int(input())
td = map(int,input().split())
r = int(input())
p_c = {i: [] for i in range(N)}
remove_child = []
# [1] parent: child
for i, d  in enumerate(td):
    if d != -1:
        # p_c.setdefault(d,[])
        p_c[d].append(i) # 부모 노드 : [자식노드]
    if i == r:
        remove_child.append(d)
# print(p_c)
{0: [1, 2], 1: [3, 4], 2: [], 3: [], 4: []}

# print(remove_child)

# [2] 제거 key
## 1. r이 child일 떄, parent에서 r을 제가
for parent in remove_child:
    if parent != -1:
        p_c[parent].remove(r)
## 2. r이 parent일 떄,child게거
rset = bfs(r) # 제거 node
# print(rset)

for child in rset:
    del p_c[child]

# [3] leaf count
cnt = 0
for node in p_c.keys():
    if not p_c[node]:
        cnt += 1
print(cnt)