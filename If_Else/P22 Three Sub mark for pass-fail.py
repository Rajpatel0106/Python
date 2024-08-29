Math = int(input("Enter Math mark ="))
Eng = int(input("Enter Eng mark ="))
Ss = int(input("Enter Ss mark ="))

total = Math + Eng + Ss
print("Total marks = ", total)
if total > 50:
    print("congratulation, You Pass")
else:
    print("Better Luck Next Time")
