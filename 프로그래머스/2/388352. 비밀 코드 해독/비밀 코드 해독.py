# 비트 연산 !!!
from itertools import combinations, permutations

def solution(n, q, ans):
    # [1]
    tmp = [idx for idx in range(1, n +1)]
    qsets = [set(row) for row in q]
    answer = 0
    total = set(combinations(tmp,5))
    #[2]
    cnt = 0
    for t in total:
        t = set(t)
        ok = True   
        for idx in range(len(q)):
            if len(t & qsets[idx]) != ans[idx]:
                ok = False
                break
        if ok:
            cnt += 1
    print(cnt)
#         temp = list(combinations(row, ans[idx]))
#         for t in temp:
#             if t not in t0:
#                 t0.remove(t)
    
        
#     print(len(t0))
#     answer = 0
    answer = cnt
    return answer
"""
[
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[3, 7, 8, 9, 10],
[2, 5, 7, 9, 10],
[3, 4, 5, 6, 7]
]
"""