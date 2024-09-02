No = int(input("Enter fuel efficiency ="))

if No <= 15:
    print("Low")
elif 16 < No < 25:
    print("Average")
elif No > 25:
    print("High")
else:
    print("Wrong")
