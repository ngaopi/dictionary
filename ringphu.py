# Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.
# For example:
a=['simple', 'is', 'better', 'than', 'complexion']
i=0
max=0
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
    i=i+1
print(max)