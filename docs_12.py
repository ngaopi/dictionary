# Q 20.Write a Python program to check a dictionary is empty or not.
a={"a":3,"b":{},"c":9,"d":{}}
for i in a:
    if a[i]=={}:
        print("empty dict")
    else:
        print(a[i])

