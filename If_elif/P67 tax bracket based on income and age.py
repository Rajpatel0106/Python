amount = int(input("Enter income ="))
age = int(input("Enter age ="))

if amount <= 30000:
    print("Low")
elif 30000 < amount <= 60000 and 18 <= age <= 50:
    print("Medium")
elif amount > 60000:
    print("High")
else:
    print("Wrong")
