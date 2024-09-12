no = int(input("Enter Number ="))
op = int(input("Enter Div Number ="))

for i in range(1, no+1):
    if i % op == 0:
        print(i)
