dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
t = 0
for i in dice_result:
    if i == 6:
        t = t + 1
print(t)
