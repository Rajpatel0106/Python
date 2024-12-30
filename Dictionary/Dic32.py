# 12. Write a Python program to get a list of all values in a dictionary.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }
# Expected Output:
# [33, 45, 30, 34]
#
# Hint: Use the values() method to get the values and convert them to a list if needed.

marks = {
    "ram": 33,
    "rahul": 45,
    "devesh": 30,
    "jayul": 34
}
# value = marks.values()
print(marks.values())