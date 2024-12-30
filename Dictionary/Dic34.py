# 14. Write a Python program to get the length of a dictionary.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16
# }
# Expected Output:
# Length of dictionary: 5
#
# Hint: Use the len() function to count the number of key-value pairs in the dictionary.

marks = {
    "ram": 33,
    "rahul": 45,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16
}
t = 0
for key,value in marks.items():
    t = t + 1
print("Length of dictionary:",t)