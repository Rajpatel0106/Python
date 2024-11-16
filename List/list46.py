lang = input("Enter Language =")
list1 = ["c", "fortran", "pascal"]
list2 = ["java", "c++", "python"]
list3 = ["haskell", "scala", "lisp"]
if lang in list1:
    print("procedural")
elif lang in list2:
    print("object_oriented")
elif lang in list3:
    print("functional")
else:
    print("Wrong language")
