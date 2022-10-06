for _ in range(int(input())):
    n,m = map(int, input().split())
    k = n//m
    print("yes") if n%m == 0 and k%2 == 0 else print("no")
