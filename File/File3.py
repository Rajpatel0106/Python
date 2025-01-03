# 1.Count number of ‘k’
f1=open("abc",'r')
t = 0
while True:
    c=f1.read(1)
    if not c:
        break
    if c == 'k':
        t = t+ 1
print("Count Of k =",t)
print("\nEnd of File")
f1.close()