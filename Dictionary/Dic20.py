# 7.Give Choice 1 for pass ,2 for fail ,3 for both
students = {11: "Rahul", 33: "Neha", 15: "Mansi", 70: "Raj", 36: "Priya",
            7: "Kiran", 22: "Dev", 25: "Param", 17: "Abhi", 19: "Diya"}
print("Number 1 For Pass")
print("Number 2 For Fail")
print("Number 3 For Both")

op = int(input("Enter Number ="))
for key,value in students.items():
    if op == 1:
        if key >= 18:
            print(key,value,"Pass")
    elif op == 2:
        if key <= 18:
            print(key,value,"Fail")
    elif op == 3:
        if key >= 18:
            print(key,value,"Pass")
        else:
            print(key,value,"Fail")
    # else:
    #     print("Wrong Option")