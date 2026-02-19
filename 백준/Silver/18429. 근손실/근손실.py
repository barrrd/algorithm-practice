"""
[1] 중량: 하루 -= k
[2] N개 kit -> 하루 마다 1개의 kit 
    kit => 중량 증가량
[3] 원하는 것은 500이상 되도록 plan

"""
from itertools import combinations, permutations
####
# [1] 
def find(nlist):
    weight = w
    for pw in nlist:
        weight += -K + pw
        if weight < 500:
            return 0
    # print(nlist)
    return 1
####
N, K = map(int,input().split())
nlst = list(map(int, input().split()))
# print(nlst)
result = 0
# print(list(permutations(nlst,len(nlst))))

w = 500
for temp in list(permutations(nlst,len(nlst))):
    result += find(temp)
print(result)