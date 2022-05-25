def func(x):
    i=0
    a=[]
    while i<len(x):
        count=0
        j=0
        b=[]
        while j<len(x):
            if x[i]==x[j]:
                count+=1
            j=j+1
        b.append(count)
        b.append(x[i])
        if b not in a:
            a.append(b)
        i=i+1
    print(a)
func(x=input("enter the character:"))       
            