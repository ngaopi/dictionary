d={'list1': [4, 7, 10, 20],'list2': [7, 16, 9, 10], 'list3': [13, 10, 4, 8], 'list4': [7, 20, 6, 11]}
# Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
b=[]
for i in d:
    b.extend(d[i])
    j=0
    c=[]
    while j<len(b):
        if b[j] not in c:
            c.append(b[j])
            c.sort()
        j=j+1
print(c)
