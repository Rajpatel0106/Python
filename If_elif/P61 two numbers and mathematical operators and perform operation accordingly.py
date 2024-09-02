# Write a program to accept two numbers and mathematical
# operators and perform operation accordingly.
# Example:
# •	Enter First Number: 7
# •	Enter Second Number: 9
# •	Enter operator: +
# •	Your Answer is: 16

op = input("Enter operator(+,-,*,/) =")
No1 = int(input("Enter Number ="))
No2 = int(input("Enter Number ="))

if op == '+':
    sum = No1 + No2
    print("Sum =", sum)
elif op == '-':
    sub = No1 - No2
    print("sub =", sub)
elif op == '*':
    mul = No1 * No2
    print("Mul", mul)
elif op == '/':
    div = No1 / No2
    print("Div", div)
else:
    print("Wrong op")