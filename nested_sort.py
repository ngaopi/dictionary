user=input("enter the word:")
b={}
for i in user:
    if i  in b:
        b[i]+=1
    else:
        b[i]=1
sorted=dict(sorted(b.items()))
for x,y in sorted.items():
    print(x,y)

