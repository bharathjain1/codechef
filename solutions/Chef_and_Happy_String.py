for i in range(int(input())):
    s = input()
    count = 0
    flag = 0
    for i in s:
        if i in ['a','e','i', 'o', 'u']:
            count = count + 1
            if count > 2:
                flag = 1
        else:
            count = 0
    if flag == 1:
        print("Happy")
    else:
        print("Sad")
        