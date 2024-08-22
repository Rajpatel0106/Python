print("Select item Number From Below Menu")
print("1.Pizza, Price=299₹")
print("2.Burger, Price=129₹")
print("3.Dosa, Price=99₹")
print("4.Sandwich, Price=149₹")
print("5.PavBhaji, Price=139₹")

op = int(input("Enter option ="))

if op == 1:
    qt = int(input("How many Pizza you want ="))
    Bill = 299 * qt
    print("Your bill is =", Bill)
elif op == 2:
    qt = int(input("How many Burger you want ="))
    bill = 129 * qt
    print("Your bill is =", bill)
elif op == 3:
    qt = int(input("How many Dosa you want ="))
    bill = 99 * qt
    print("Your bill is =", bill)
elif op == 4:
    qt = int(input("How many Sandwich you want ="))
    bill = 149 * qt
    print("Your bill is =", bill)
elif op == 5:
    qt = int(input("How many PavBhaji you want ="))
    bill = 139 * qt
    print("Your bill is =", bill)
else:
    print("Wrong option")
