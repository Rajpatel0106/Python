# 11. Write a Python program to get a list of all keys in a dictionary.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }
#
# Expected Output:
# ["ram", "rahul", "devesh", "jayul"]
#



# Hint: Use the keys() method to obtain the keys and convert them to a list if needed.

marks = {
    "ram": 33,
    "rahul": 45,
    "devesh": 30,
    "jayul": 34
}
# key = marks.keys()
print(marks.keys())