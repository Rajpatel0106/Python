# 13. Write a Python program to print only the students
# who failed from the dictionary (marks < 18).
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
# rahul    15     fail
# jiya     16     fail
# sadhana  11     fail

# Hint: Use a loop and conditional statements to filter and display students who failed.

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
print("Name","Mark","Result")
for key,value in marks.items():
    if value <= 18:
        print(key,value,"Fail")