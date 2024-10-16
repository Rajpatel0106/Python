#  5X4X3X2X1

n = int(input("Enter number ="))
i = n
f = 1

while i >= 1:
    print(i, end=" X ")
    f = f * i
    i = i - 1
print("\nFactorial =", f)
