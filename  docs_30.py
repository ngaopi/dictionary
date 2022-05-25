# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

dict ={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a={x.replace(' ', ''):y
    for x,y in dict.items()}
print (a)