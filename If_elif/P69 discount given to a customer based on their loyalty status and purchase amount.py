amount = int(input("Enter purchase amount ="))
loy = input("Enter loyalty status =")

if loy == 'Loyal' and amount > 2000:
    print("20% discount applies")
elif loy  == 'Non-Loyal' and amount > 2000:
    print("10% discount applies")
elif amount < 2000:
    print("no discount applies")
else:
    print("wrong input")
