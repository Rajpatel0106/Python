import random
d1={}

n=int(input("Enter limit =>"))
for i in range(1,n+1):
    k=i
    v=random.randint(1,30)
    d1[k]=v

print("No\tMarks")
print("*"*30)
for k,v in d1.items():
    print(k,"\t",v)
print("*"*30)