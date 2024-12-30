# 3. Write a Python script to check whether a given key already exists in a dictionary.
#
# Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "manav": 30,
#     "jayul": 34,
#     "meena": 29,
#     "siddhi": 48
# }
# Enter key for search: rahul
# Output:
# Yes, it exists.
#
# Hint: Use the in keyword to check if the key is present in the dictionary.

marks = {
        "ram": 33,
        "rahul": 45,
        "manav": 30,
        "jayul": 34,
        "meena": 29,
        "siddhi": 48
    }

name = input("Enter key for search=")

if name in marks:
    print("Yes, it exists")
else:
    print("Not exists")