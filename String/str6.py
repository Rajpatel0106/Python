text = input("Enter Text =")
c = 0
c1 = 0
for i in text:
    if i.isupper():
        c = c + 1
    else:
        c1 = c1 + 1
print("Uppercase =",c)
print("Lowercase =",c1)