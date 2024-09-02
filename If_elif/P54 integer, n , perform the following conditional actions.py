No = int(input("Enter Number ="))

if No % 2 != 0:
    print("Weird")
elif No % 2 == 0 and 2 <= No <= 5:
    print("Not Weird")
elif No % 2 == 0 and 6 <= No <= 20:
    print("Weird")
elif No % 2 == 0 and No > 20:
    print("Not Weird")
else:
    print("wrong input")
