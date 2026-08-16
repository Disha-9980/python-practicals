a = []
for i in range(10):
    b = int(input(""))
    a.append(b)

print ("In list: ", a)
print ("Max =", max(a))
print ("Min =", min(a))

total = sum(a)
average = total/len(a)

print ("Sum =", total)
print ("Average =", average)

print ("Even numbers:")
for num in a:
    if num % 2 == 0:
        print (num)

print ("Odd numbers:")
for num in a:
    if num % 2 != 0:
        print (num)