Price = int(input("Enter Market price ="))

if Price > 10000:
    amount = Price * 20/100
    net = Price - Price * 20/100
    print("20% Discount =", amount)
    print("Net Amount  =", net)
elif Price > 7000 or Price <= 10000:
    amount = Price - 15
    net = Price - Price * 15/100
    print("15% Discount =", amount)
    print("Net Amount  =", net)
elif Price >= 7000:
    amount = Price - 10
    net = Price - Price * 10/100
    print("10% Discount =", amount)
    print("Net Amount  =", net)
else:
    print("No Discount Below 7000")