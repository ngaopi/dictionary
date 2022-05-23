# s='w3resources'
# dict={}
# for i in s:
#     dict[i]=dict.get(i,0)+1
# print(dict)

a='w3resources'
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
print(b)
