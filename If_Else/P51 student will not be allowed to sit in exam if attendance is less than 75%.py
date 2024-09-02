held = int(input("Enter Number of classes held ="))
att = int(input("Enter Number of classes attended ="))

per = att / float(held)*100
print("percentage of class attended =", per)

if per >= 75:
    print(per, "You allowed to sit in exam")
else:
    print(per, "You Not allowed to sit in exam")
