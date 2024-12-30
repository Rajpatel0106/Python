# 9. Write a Python program to count the number of students
# who passed (marks >= 18) in the dictionary.
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
#     "karan": 20,
#     "anita": 25
# }
# Expected Output:
#
# Number of passed students: 5
#
# Hint: Use a loop and a counter variable to keep track of the number of students who meet the passing criteria.

marks = {
        "ram": 33,
        "rahul": 15,
        "devesh": 30,
        "jayul": 34,
        "jiya": 16,
        "sadhana": 11,
        "meena": 19,
        "karan": 20,
        "anita": 25
    }
t = 0
for key,value in marks.items():
    if value >= 18:
        t = t + 1
print("Number of passed students:",t)