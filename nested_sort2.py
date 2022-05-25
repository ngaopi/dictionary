a=[]
b=[]
for i in range(0,3,1):
    user=input("enter the values:")
    user1=int(input("enter the keys:"))
    a.append(user)
    b.append(user1)
    c=[]
    for j in range(i):
        c.append(a[j])
        c.append(b[j])
print(c)
        # c[a[j]]=b[j]
# sorted=dict(sorted(c.items()))
# print(sorted)




