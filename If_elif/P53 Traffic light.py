light = input("Enter Light Color =")

if light == 'Green':
    print("Car is allowed to go")
elif light == 'Yellow':
    print("Car has to wait")
elif light == 'Red':
    print("Car has to stop")
else:
    print("unrecognized signal")
