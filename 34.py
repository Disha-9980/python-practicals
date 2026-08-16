a = int(input("Enter number: "))

if a < 2:
    print("Not a Prime")
else:
    Prime = True
    for i in range(2, a):
        if a % i == 0:
            Prime = False
            break

    if Prime:
        print("Prime")
    else:
        print("Not Prime")