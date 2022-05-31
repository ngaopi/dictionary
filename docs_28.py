# Q28.Write a Python program to convert a list into a nested dictionary of keys.

# Sample output:
# {1: {2: {3: {4: {}}}}}
a= [1, 2, 3, 4]
temp={}
i=len(a)-1
while i>=0:
    d = {}
    k=a[i]
    d[k]=temp
    temp = d
    i=i-1
print(d)
