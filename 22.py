a = int(input("num 1 : "))
b = int(input("num 2 : "))
c = int(input("num 3 : "))

if a > b:
    if a > c:
        print("largest : ", a)
    else:
        print("largest : ", c)
else:
    if b > c:
        print("largest : ", b)
    else:
        print("largest : ", c)