# 1 X 2 X 3 X 4 x 5
# t = 120

n = int(input("Enter Number ="))
i = 1
f = 1
while i <= n:
    print(i, end=" X ")
    f = f * i
    i = i + 1
print("\nFactorial = ", f)
