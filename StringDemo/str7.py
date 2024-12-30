text = input("Enter Text =")
c = 0
for i in text:
    if i == " ":
        c = c + 1
print("Space Count =",c)