t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    sum =  a-b
    print(b) if sum > b else print(sum)