def num(x):
    i=0
    d=int(input("enter the number:"))
    while i<len(x):
        b=d%len(x)
        if b==i:
            return x[i]
        i=i+1            
print(num(["i love","you","i miss u","i need","you","my world"]))
    


