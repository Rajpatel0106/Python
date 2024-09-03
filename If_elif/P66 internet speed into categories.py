speed = int(input("Enter internet speed (Mbps) ="))

if speed <= 5:
    print("Slow Speed")
elif 6 <= speed <= 20:
    print("Average Speed")
elif 21 <= speed <= 50:
    print("Fast Speed")
elif speed > 50:
    print("Very Fast")
else:
    print("Wrong")
