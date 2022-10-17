# cook your dish here
try:
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        k=21-(a+b)
        if 1<=k<=10:
            print(k)
        else:
            print('-1')
except:
    pass

        
        
