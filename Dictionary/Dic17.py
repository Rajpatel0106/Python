# 4.Display Pass/Fail along with count of pass and fail students
students = {11: "Rahul", 33: "Neha", 15: "Mansi", 70: "Raj", 36: "Priya",
            7: "Kiran", 22: "Dev", 25: "Param", 17: "Abhi", 19: "Diya"}
t = 0
t1 = 0
for key,value in students.items():
    if key >=18:
        t = t + 1
    else:
        t1 = t1 + 1
print("Pass =",t)
print("Fail =",t1)
