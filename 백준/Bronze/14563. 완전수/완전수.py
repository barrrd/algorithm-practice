import sys
input = sys.stdin.readline

"""
[1] 완전수: 약수에서 저기하나 뺸 것의 합이 자신인 경우
[2] 부족수: 약수의 합의 자기보다 작은 거
[3] 과잉수:            자기보다 큰 거
"""
T = map(int,input())
darr  = list(map(int,input().split()))

for arr in darr:
    tmp = set()
    for i in range(1,int(arr**(0.5)) + 1):
        if arr % i == 0:
            tmp.add(i)
            tmp.add(arr // i)
    tlst = list(tmp)
    tlst.sort()

    real = tlst.pop(-1)
    sum_tmp = 0
    for i in tlst:
        sum_tmp += i
    if sum_tmp == real:
        print("Perfect")
    elif real < sum_tmp:
        print("Abundant")
    else:
        print("Deficient")
