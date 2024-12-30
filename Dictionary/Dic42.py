import random
d1={}
t = 0
t1 = 0
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    k=i
    v=random.randint(1,30)
    d1[k]=v

print("No\tMarks")
print("*"*30)
for k,v in d1.items():
    if v>18:
        print(k,"\t",v,"\tPass")
        t = t + 1
    else:
        print(k, "\t", v, "\tFail")
print("*"*30)
print("Pass Student =",t)
