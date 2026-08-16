for a in range(2, 51):
    Prime = True
    for i in range(2, a):
        if a % i == 0:
            Prime = False
            break
    if Prime:
        print(a)