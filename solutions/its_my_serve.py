t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    r=(p+q)//2
    if r%2==0:
        print("Alice")
    else:
        print("Bob")