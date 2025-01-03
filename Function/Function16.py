# User defined – Arbitrary Argument
def pdata(*name):
    for x in name:
        print(x)

pdata("Ram","Lakhan","Arjun","Karna")

print("*"*20)

pdata("Ram","Lakhan","Arjun")

# 3
def pdata(*a):
    print("\nValues")
    for no in a:
        print(no,end='')
pdata(1,2,3,4,5,6)
pdata(1,2,3)

