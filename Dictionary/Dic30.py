# 10. Write a Python program to update a dictionary with new student marks.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45
# }
# Enter new data:
# devesh 30
# Expected Output:
# {"ram": 33, "rahul": 45, "devesh": 30}
#
# Hint: Use the syntax dict[key] = value to add new key-value pairs.
#

marks = {
    "ram": 33,
    "rahul": 45
}

name =input("Enter Student Name :")
mrk = int(input("Enter Mark :"))
marks[name] = mrk
print(marks)