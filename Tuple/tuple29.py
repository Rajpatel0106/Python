no = int(input("Enter value for delete ="))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
list1.remove(no)
t1 = tuple(list1)
print(t1)