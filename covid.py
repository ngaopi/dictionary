
a=[4,5,3,2,7,8]
covid=int(input("enter the covid place:"))
place=int(input("enter my place:"))
step=int(input("enter the step:"))
i=0
while i<len(a):
    j=0
    while j<len(a):
        d=a[i],a[j]
        i=i+step
if d==covid:
    print("yes")
else:
    print("no")
    
    