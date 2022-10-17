for _ in range(int(input())):
    s = input()
    t = input()
    i = 0
    r = ""
    while i < len(s):
        if s[i] == t[i]:
            r = r + 'G'
            i = i+1
        else:
            r = r + 'B'
            i = i + 1
    print(r)