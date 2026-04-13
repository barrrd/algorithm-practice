n = int(input())

MOD = 1_000_000_000

if n == 0:
    print(0)
    print(0)
else:
    k = abs(n)

    a, b = 0, 1
    for _ in range(k):
        a, b = b, (a+b)% MOD


    if n > 0:
        sign = 1
    else:
        if k % 2 == 1:
            sign = 1
        else:
            sign = - 1

    print(sign)
    print(a)

