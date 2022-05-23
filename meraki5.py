# list1=['one','two','three','four','five']

# list2=[1,2,3,4,5,]
# Output : {'one':1,'two':2,'three':3,'four':4,'five':5}

list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]
# for d in list1:
#     d=dict(zip(list1,list2))
# print(d)
i=0
b={}
while i<len(list1):
    b[list1[i]]=list2[i]
    i=i+1
print(b)