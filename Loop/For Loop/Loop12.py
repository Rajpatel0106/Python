# 1 * 2 * 3 * 4 * 5 *

no = int(input("Enter No ="))
c = 1
for i in range(1, no + 1):
    print(i, end=" * ")
    c = c * i
print("Total =", c)
