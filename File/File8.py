# 6.Print Without Space
f1=open("abc",'r')
while True:
    c=f1.read(1)
    if not c:
        break
    if c ==' ':
        print('',end="")
    else:
        print(c,end="")
print("\nEnd of file")
f1.close()
