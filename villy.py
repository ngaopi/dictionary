a=[6,1,3,6,5,3,2]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        if a[i] not in b:
            b.append(a[i])
        e=a[j]*a[j]
        sum+=e
        j=j+1
    i=i+1
print(b,sum)