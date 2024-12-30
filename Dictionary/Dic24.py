# 4. Write a Python script to print data in vertical form and
# display whether that student is pass or fail from the dictionary.
# (18 marks to pass)
# Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }
#
marks = {"ram": 33,"rahul": 15,"devesh": 30,"jayul": 34,
         "jiya": 16,"sadhana": 11,"meena": 19,"karan": 20}
print("Name","Mark","Result")
for key,value in marks.items():
    if value >=18 :
        print(key, value, "Pass")
    else:
        print(key, value, "Fail")
