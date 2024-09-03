amount = int(input("Enter Total Purchases ="))
year = int(input("years of membership ="))

if amount > 5000 and year > 2:
    print("Upgrade eligible")
else:
    print("No upgrade")
