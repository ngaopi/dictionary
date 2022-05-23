# Q24.Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j] in b:
            d=a[j]+a[i]
        else:
            b.append(a[i])
        j=j+1
    i=i+1
print(b)

