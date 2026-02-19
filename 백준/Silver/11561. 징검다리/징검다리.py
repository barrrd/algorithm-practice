import sys
input = sys.stdin.readline

def can(k, N):
    return k*(k+1)//2 <= N

T = int(input())
for _ in range(T):
    N = int(input().strip())
    lo, hi = 0, 2*10**8  # k ≈ sqrt(2N) ≤ ~1.5e8 (N ≤ 1e16) 넉넉히 잡음
    while lo < hi:
        i = 1
        # print(i)
        mid = (lo + hi + 1) // 2
        if can(mid, N):
            lo = mid
        else: 
            hi = mid - 1
        # i +=1
    print(lo)