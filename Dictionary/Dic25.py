# 5. Write a Python script to print data in vertical form and
# display only pass students from the dictionary. (18 marks to pass)
#
# Sample data:
#
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
# Expected Output:
# name     mark   result
# ram      33     pass
# devesh   30     pass
# jayul    34     pass
# meena    19     pass
# karan    20     pass
#
# Hint: Filter the results based on the passing criteria while printing.

marks = {
        "ram": 33,
        "rahul": 15,
        "devesh": 30,
        "jayul": 34,
        "jiya": 16,
        "sadhana": 11,
        "meena": 19,
        "karan": 20
    }
print("Name"," Mark"," Result")
for key,value in marks.items():
    if value >= 18:
        print(key," ",value," ","Pass")