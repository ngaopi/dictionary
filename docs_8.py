# Q13.Write a Python program to sum all the items in a dictionary.
# a={1:2,2:4,3:6,4:8}
# sum=0
# for i in a:
#     sum=sum+a[i]
#     sum=sum+i
# print(sum)

# Q14.Write a Python program to multiply all the items in a dictionary.
a={1:2,3:4,5:9}
for i in a:
    d=a[i]*a[i]
    a[i]=d
print(a)