a={1:['jean castro'],2:['lula powell'],3:['brian howell'],4:['lynne foster'],5:['zachary simon']}
e={}
for j in a:
    x=a[j]
    i=0
    b=[]
    while i<len(x):
        e[j]=x[i]
        b.append(e)
        i=i+1
print(b)
