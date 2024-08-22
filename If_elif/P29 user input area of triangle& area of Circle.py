print("find area of triangle choose no1")
print("find area of Circle choose no2")
op = int(input("Enter Number ="))

if op == 1:
    h = float(input("enter Height ="))
    b = float(input("enter base ="))
    aot = h * b * 0.5
    print("area of triangle =", aot)
elif op == 2:
    r = float(input("Enter Radius ="))
    aoc = 3.14 * r * r
    print("area of Circle =", aoc)
else:
    print("wrong op")
