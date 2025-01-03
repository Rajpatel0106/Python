# 2.Count number of ‘space’
f1=open("abc",'r')
t = 0
while True:
    c=f1.read(1)
    if not c:
        break
    if c == ' ':
        t = t + 1
print("Count Of Space =",t)
print("\nEnd of file")
f1.close()
