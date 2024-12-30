# 6.Enter name and display record
students = {11: "Rahul", 33: "Neha", 15: "Mansi", 70: "Raj", 36: "Priya",
            7: "Kiran", 22: "Dev", 25: "Param", 17: "Abhi", 19: "Diya"}
Name = input("Enter Name =")
for key,value in students.items():
    if Name == value:
        print(key,":",value)
    else:
        print("None")
