Sub = ["PP1", "CCF", "SAE", "WAS"]

print ("list = ", Sub)
print ("First = ", Sub [0])
Sub [1] = "cloud"
print ("Modify = ", Sub)

Sub.append ("EP")
print ("Append = ", Sub)

Sub.remove ("EP")
print ("Remove = ", Sub)

Sub.insert (0, "EH")
print ("Insert = ", Sub)

removed = Sub.pop ()
print ("Pop = ", removed)
print ("Final = ", Sub)