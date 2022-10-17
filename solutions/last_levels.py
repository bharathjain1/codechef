t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if x<4:
        print(x*y)
    elif x%3 ==0: 
        print(x*y + int((x/3)-1)*z)
    else:
        print(x*y + int((x//3))*z)


