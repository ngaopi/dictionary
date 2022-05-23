# Question 11

# Write a program to print the top 3 highest values of a given dictionary.
# Input :-
# Code Example
# my_dict = {
#  'a':50, 
#  'b':58, 
#  'c':56,
#  'd':40, 
#  'e':100, 
#  'f':20
#  }
# Output :-
# [58,56,100]
dic={'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# max=0
# for i in dic:
#     if dic[i]>max:
#         max=dic[i]
# print(max)
x=0
y=0
z=0
k=[]
for i in dic:
    for j in dic:
        if dic[j]>x:
            x=dic[j]
            a=[j]
        elif dic[j]>y and dic[j]<x:
            y=dic[j]
            b=[j]
        elif dic[j]>z and dic[j]<y:
            z=dic[j]
            c=[j]
k.append(a)
k.append(b)
k.append(c)
print(k)