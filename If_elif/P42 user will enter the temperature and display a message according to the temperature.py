Temp = int(input("Enter Temp ="))

if Temp <= 0:
    print("freezing Atmosphere")
elif Temp <= 10:
    print("very cold atmosphere")
elif Temp <= 20:
    print("Cold Atmosphere ")
elif Temp <= 30:
    print("normal Atmosphere")
elif Temp <= 40:
    print("hot atmosphere")
else:
    print("very hot atmosphere")
