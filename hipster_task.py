socks = list(map(int,input().split()))
red = socks[0]
blue = socks[1]
count_fash = min(red, blue)
count_notfash = (red - min(red, blue) + blue - min(red, blue)) / 2

print(count_fash, int(count_notfash))
