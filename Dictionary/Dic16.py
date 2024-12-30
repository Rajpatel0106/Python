# 3.Display only Pass students
students = {11: "Rahul", 33: "Neha", 15: "Mansi", 70: "Raj", 36: "Priya",
            7: "Kiran", 22: "Dev", 25: "Param", 17: "Abhi", 19: "Diya"}
for key,value in students.items():
    if key >= 18:
        print(key,value,"Pass")
