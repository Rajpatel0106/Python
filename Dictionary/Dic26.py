# 6. Write a Python program to sum all the items in a dictionary.
#
# Sample data:
#
# items = {
#     "maggie": 20,
#     "parleg": 10,
#     "crackjack": 20,
#     "noodles": 32,
#     "chips": 15,
#     "cookies": 18
# }
# Expected Output:
# 125 Rs
#
# Hint: Use the sum() function combined with values() to calculate the total.

items = {
        "maggie": 20,
        "parleg": 10,
        "crackjack": 20,
        "noodles": 32,
        "chips": 15,
        "cookies": 18
    }

value = items.values()
print(sum(value),"Rs")