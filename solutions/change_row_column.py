t = int(input())
for _ in range(t):
    sx,sy,ex,ey = map(int, input().split( ))
    print(1) if sx != ex and sy != ey else print(2)