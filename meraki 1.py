# Question 1
# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
# Example :-
# Input :-
# Code Example

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# Output :{1: 10, 2: 60, 3: 30, 5: 50, 6: 60}

dict1={1:10, 2:20}
dict2={3:30,2:40}
dict3={5:50,6:60}
for i in dict1:
    for j in dict2:
        if i==j:
            dict3[i]=dict1[i]+dict2[j]
        else:
            dict3[i]=dict1[i]
            dict3[j]=dict2[j]
print(dict3)
            
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)

    
