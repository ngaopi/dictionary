# question7
# Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
# Example :-
# Input :-
# Code Example

dic=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# Output :-
# ['2', '7', '9', '5', '1']
i=0
b=[]
while i<len(dic):
    for j in dic[i]:
        if dic[i][j]not in b:
            b.append(dic[i][j])
        i+=1
print(b)
            