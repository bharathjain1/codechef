t = int(input())
for i in range(t):
    n,x,k = map(int,input().split())
    if x>k:
        print(0)
    elif (n*x > k):
        print(k//x)
    else:
        print(n)
        