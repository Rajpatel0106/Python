text = input("Enter Text =")
c = 0
for i in text:
    if i in ['a','e','i','o','u']:
        c = c + 1
print(c)