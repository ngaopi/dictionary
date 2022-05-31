def num(a,b):
    i=0
    while i<len(a):
        j=0
        c=[]
        while j<len(a)-1:
            if b in a:
                d=[a[j],a[j+1]]
                c.append(d)
            j=j+1
        i=i+1
    return c
print(num(a=[1,2,3,4,5],b=(int(input("enter the number:")))))
