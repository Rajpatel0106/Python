print("Press 1 for Sum ")
print("Press 2 for Sub ")
print("Press 3 for Mul ")
print("Press 4 for Div ")
op = int(input("Enter Selected Number ="))

op1 = int(input("Enter Number1 ="))
op2 = int(input("Enter Number2 ="))

if op == 1:
    sum = op1 + op2
    print("Sum =", sum)
elif op == 2:
    sub = op1 - op2
    print("Sub =", sub)
elif op == 3:
    mul = op1 * op2
    print("Mul =", mul)
elif op == 4:
    div = op1 / op2
    print("Div =", div)
else:
    print("Wrong Number")