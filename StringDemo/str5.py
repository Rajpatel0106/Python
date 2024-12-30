text = input("Enter Text =")
c = 0
c1 = 0
for i in text:
    if i in i.lower():
        print(i.upper(),end="")
        c = c+1
    elif i in i.upper():
        print(i.lower(),end="")
        c1 = c1+1
print("\nLowercase Count =",c)
print("Uppercase Count =",c1)