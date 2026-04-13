def percentage(x1,x2):
    return x2 * 100 // x1


x, y = map(int,input().split())

curr_d = percentage(x,y)

lo = 1
hi = 10**9
ans = -1
while lo <= hi:
    mid = (lo + hi)// 2

    if percentage(x+mid,y+mid) > curr_d:
        hi = mid - 1
        ans = mid
    else:
        lo = mid + 1

print(ans)
