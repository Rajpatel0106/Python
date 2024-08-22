print("Find Positive-Negative choose no1")
print("Find odd-even choose no2")

op = int(input("Enter Number ="))

if op == 1:
    no = int(input("Enter Number ="))
    if no >= 0:
        print(no, "is Positive")
    else:
        print(no, "Negative")
elif op == 2:
    no = int(input("Enter Number ="))
    if no % 2 == 0:
        print(no, " is even")
    else:
        print(no, " is odd")
else:
    print("wrong input")
