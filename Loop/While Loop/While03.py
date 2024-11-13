# 2)1 is odd
# 2 is even

n = int(input("Enter Number ="))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is odd")
    i = i + 1
