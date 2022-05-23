# Question 14
# Write a program to sort a dictionary in ascending or descending according to its values .
# Input :-
# Code Example
# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}
# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

a={'babe':45,'ring':60,'hun':20,'love':30,'moha':50}
b=sorted(a.items(),key=lambda x:x[1],reverse=True)
for i in b:
    print(i[0],i[1])
# for i in a:
#     for j in a:
#         if a[j]>a[i]:
#             a[j],a[i]=a[i],a[j]
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)