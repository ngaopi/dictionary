d={"a":[3,6,2,5],"b":[3,1,1,8]}
# e={}
# for j in d:
#     x=d[j]
#     i=-1
#     b=[]
#     while i>=-len(x):
#         b.append(x[i])
#         i=i-1
#     e[j]=b
# print(e)
e={} 
for j in d:
    x=d[j]
    sum=0
    i=0
    while i<len(x):
        sum=sum+x[i]
        i=i+1
    e[j]=sum
print(e)