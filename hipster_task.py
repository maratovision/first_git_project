socks = list(map(int,input().split()))
a = socks[0]
b = socks[1]
count_fash = 0
count_notfash = 0
if a > b:
    a = a - b
    if a > 1:
        count_notfash = a // 2
    print(b, count_notfash)
elif a < b:
    b = b - a
    if b > 1:
        count_notfash = b // 2
    print(a, count_notfash)
    else:
        b = 0