# Print only even values, sum and count it
def even(no):
    # no = int(input("Enter Number ="))
    t = 0
    c = 0
    for i in range(1,no+1):
        if i % 2 == 0:
            print(i)
            t = t + 1
            c = c + i
    print("Count =",t)
    print("Sum =",c)
even( no = int(input("Enter Number =")))