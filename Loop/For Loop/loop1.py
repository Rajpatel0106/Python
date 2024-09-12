from colorama import Back, Style
no = int(input("Enter Number ="))
op = int(input("Enter Div Number ="))
c = 0
for i in range(1, no + 1):
    if i % op == 0:
        print(i, end="")
        c = c + 1
print(Back.RED + "Total =" + Style.RESET_ALL, c)
