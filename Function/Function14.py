# User defined – Default Argument
def add(a,b,c,d,e):
    print("Add = ",a+b+c+d+e)
add(11,22,33,44,55)

def add(a,b,c,d,e):
    print("Add = ",a+b+c+d+e)
add(11,22,33,44,55)
add(11,22,33,44)
add(11,22,33)
add(11,22)

# 2
# User defined – Default Argument
def add(a,b,c=0,d=0,e=0):
    print("Add = ",a+b+c+d+e)

add(11,22,33,44,55)
add(11,22,33,44)
add(11,22,33)
add(11,22)

# 3
def mul(a,b,c=0,d=0,e=0):
    print("Mul = ",a+b+c+d+e)

mul(11,22,33,44,55)
mul(11,22,33,44)
mul(11,22,33)
mul(11,22)

# 4
# User defined – Default Argument
def mul(a,b,c=1,d=1,e=1):
    print("Mul = ",a*b*c*d*e)

mul(1,2,3,4,5)
mul(1,2,3,4)
mul(1,2,3)
mul(1,2)

