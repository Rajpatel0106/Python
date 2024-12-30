# 8. Write a Python program to find the maximum and minimum marks from a dictionary.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }
# Expected Output:
#
# Max: 45, Min: 18
#
# Hint: Use max() and min() functions on values() to find the highest and lowest marks.

marks = {
        "ram": 33,
        "rahul": 45,
        "devesh": 30,
        "jayul": 34,
        "meena": 29,
        "karan": 40,
        "anita": 18,
        "siddhi": 25
    }
value = marks.values()
print("Max: ",max(value),"Min: ",min(value))