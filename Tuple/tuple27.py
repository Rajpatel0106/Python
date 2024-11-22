no = int(input("Enter value for search:"))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
if no in t1:
    print("Yes", no, "is there")
else:
    print("No", no, "is not there")