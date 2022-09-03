for i in range(1, 200):
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num = num+1
    if (num == 2):
        print(i)
