No1 = int(input("Enter Buying Price ="))
No2 = int(input("Enter Selling Price ="))

Total = No1 - No2

if Total > 0:
    print(Total, "Profit")
else:
    print(Total, "Loss")
