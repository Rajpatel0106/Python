temp = float(input("Enter Temperature ="))

if temp <= 10:
    print("Cold")
elif 10 < temp and temp < 25:
    print("Warm")
elif temp > 25:
    print("Hot")
else:
    print("Wrong Temp")
