# question3
# Ek program likhiye jo ki dictionaries ki values ka sum print kare.
# Example :-
# Input :-
# Code Example
# my_dict = {
#   'data1':100,
#   'data2': -54,
#   'data3': 247
#    }
# Output :-
# 293
dict={"data1":100,"data2":-54,"data3":247}
val=dict.values()
sum=0
for i in val:
    sum=sum+i
print(sum)    