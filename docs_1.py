
# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 100, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:
    for j in d2:
        if i==j:
            d1[i]=d1[i]+d2[j]
d2.update(d1)
print(d2)

