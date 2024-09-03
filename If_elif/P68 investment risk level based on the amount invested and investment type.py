amount = int(input("Enter amount invested ="))
inv = input("Enter investment type =")

if amount <= 10000 and inv == 'savings account':
    print("Low Risk")
elif 10001 < amount < 50000 and inv == 'Mutual funds':
    print("Medium Risk")
elif amount > 50000 and inv == 'stocks':
    print("High Risk")
else:
    print("Wrong")
