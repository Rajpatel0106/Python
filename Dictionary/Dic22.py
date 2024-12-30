# 2. Write a Python script to print data in vertical form from a dictionary.
#
# Sample data:
#
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }
# Expected Output:
# ram    33
# rahul  45
# devesh 30
# jayul  34
# meena  29
# nisha  37
# karan  40
# anita  18
# siddhi 25
# Hint: Use a loop to iterate through the dictionary items and print each key-value pair.

marks = {
        "ram": 33,
        "rahul": 45,
        "devesh": 30,
        "jayul": 34,
        "meena": 29,
        "nisha": 37,
        "karan": 40,
        "anita": 18,
        "siddhi": 25
}
for key,value in marks.items():
    print(key,value)