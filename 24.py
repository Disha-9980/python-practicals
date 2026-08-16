a = float(input("num 1 : "))
b = float(input("num 2 : "))
c = input("operator (+, -, *, /) : ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("cannot divide")
else:
    print("Invalid operator")