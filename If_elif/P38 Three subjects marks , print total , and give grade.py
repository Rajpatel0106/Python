Maths = int(input("Enter Maths Mark ="))
Eng = int(input("Enter English Mark ="))
Sci = int(input("Enter Science Mark ="))

Total = Maths + Eng + Sci
print("Total =", Total)

if Total >= 100:
    print("Grade A")
elif Total >= 50:
    print("Grade B")
else:
    print("Grade C")
