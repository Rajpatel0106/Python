pay = int(input("Enter number of missed payments ="))

if pay == 0:
    print("Excellent")
elif 1 <= pay <= 2:
    print("Good")
elif 3 <= pay <= 5:
    print("Fair")
elif pay > 5:
    print("Poor")
else:
    print("Wrong Input")
