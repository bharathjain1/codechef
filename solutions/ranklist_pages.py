import math

t = int(input())
pages = 0
for i in range(t):
    a = int(input())
    if a <= 25:
        pages = 1
    else:
        pages = a/25
    print(math.ceil(pages))
    
