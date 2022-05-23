# Question 6

# Write a program to remove duplicate keys.
# Example :-
# Input :-
# Code Example

# dic={
# “ball”:”red”,
# ”bat”:4,
# ”wickets”:8,
# ”ball”green,
# ”bat”:3
# }
# Output :-{“ball”:”red”,”bat”:4,”wickets”:8}

dic={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3,'bat':6 }
b={}
for i in dic:
    if i not in b:
        b[i]=dic[i]
print(b)
