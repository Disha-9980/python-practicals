a = 10
b = 5.5

result = a + b

print ("Implicit type:")
print ("int value =", a)
print ("float value =", b)
print ("Result =", result)
print (type (result))

print ("Explicit Type:")
c = "20"
d = int(c)
print ("str to int =", d)
e = "10.5"
f = float(e)
print ("str to float =", f)
x = 25
y = str(x)
print ("int to str =", y)