t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    flag = 0
    count = 0
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            count = count + 1
            if count >= 4:
                flag = 1
        else:
            count = 0
    if flag == 1:
        print("NO")
    else:
        print("YES")