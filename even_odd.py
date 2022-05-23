a={"a":[3,2,6,1,7],"b":[9,8,4,3,1]}
for j in a:
    i=0
    b=[]
    while i<len(a[j]):
        if a[j][i]%2==0:
            b.append(a[j][i])
        i=i+1
    a[j]=b
print(a)
