#1 + 3 + 5 + 7 + 9

no = int(input("Enter Number ="))
t = 0

for i in range(1, no + 1):
    print(i*i, end="+")
    t = t + i * i
print("Total =", t, end="")
