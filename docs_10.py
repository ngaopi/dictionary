# Q8.Write a Python program to get the maximum and minimum value in a dictionary.
# a={"a":34,"b":1,"c":9,"d":-56}
# b=[]
# for x in a:
#     b.append(a[x])
#     i=0
#     min=b[i]
#     while i<len(b):
#         if b[i]<min:
#             min=b[i]
#         i+=1
# print("minimum =",min)
     
a={"a":34,"b":1,"c":9,"d":56}  
max=0
for i in a:
    if a[i]>max:
        max=a[i]
print(max)
 