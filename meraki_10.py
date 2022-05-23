# Question 10
# Count the total number of items from the values of the dictionary which are in the form of a list.
# Input :-
# Code Example
# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# Output :-
# Code Example
# total count:5
dict1={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in dict1:
    for j in dict1[i]:
        if dict1[i]:
            c=c+1
print("total count:",c)



