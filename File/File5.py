# 3.Count number of Vowels
f1=open("abc",'r')
t = 0
while True:
    c=f1.read(1)
    if not c:
        break
    if c == 'a' or c == 'e' or c =='i' or c =='o' or c =='u':
        t = t + 1
print("Count Of Vowels =",t)
print("\nEnd of file")
f1.close()
