d={"a":[10,30,60],"b":[20,40,50],"c":[30,15,25]}
e={}
for i in d:
    x=d[i]
    sum=0
    j=0
    while j<len(x):
        sum=sum+x[j]
        f=sum//3
        j=j+1
    e[i]=f
print(e)
        
    