# 1. init
n, l, w, h = map(int,input().split())

# 2. binary search
lo = 0
hi = min(l, w, h)
ans = 0
for _ in range(100):
    mid = (lo+ hi)/ 2

    if (l//mid)*(w//mid)*(h//mid) >= n:
        lo = mid 
        
    else:
        hi = mid 
print(f"{lo:.10f}")