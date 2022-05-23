#1. copy() method
# d={1:2,3:4,5:6}
# d.copy()
# print(d)
#O/P {1:2,3:4,5:6}

#2. clear() method
# d={1:2,3:4,5:6}
# d.clear()
# print(d)
#O/P {}

#3. items()method
# d={1:2,3:4,5:6}
# for x,y in d.items():
#     print(x,y)
#O/P 1 2
#    3 4
#    5 6

# d={1:2,3:4,5:6}
# b=d.items()
# print(b)
#O/P [(1,2),(3,4),(5,6)]

# d={1:2,3:4,5:6}
# d.items()
# print(d)
# {1:2,3:4,5:6}


#4. pop() method
# d={1:2,3:4,5:6}
# d.pop(1)
# print(d)
#O/P {1:2,5:6}

#5. popitem() method
# d={1:2,3:4,5:6}
# d.popitem()
# print(d)
# O/P{1:2,3:4}

#6. fromkeys() method
# d={'a','b','c'}
# y=0
# c=dict.fromkeys(d,y)
# print(c)
# O/P {'a':0,'b':0,'c':0}

#7.update()methods
# d={1:2,3:4,5:6}
# e={8:0,9:9}
# d.update(e)
# print(d)
# O/P {9:0}

#8. key()method
# a={1:2,3:4,5:6}
# d=a.keys()
# print(d)
# O/P{1,3,5}

#9. value() method
# a={1:2,3:4,5:6}
# d=a.values()
# print(d)
#O/P {2,4,6}

#10. setdefault() method
# a={1:2,3:4,5:6}
# print(a.setdefault("lo","no ID"))
# print(a.setdefault(1))
# print(a)

#11. get()method
# a={1:2,3:4,5:6}
# b=a.get(1)
# print(b)

#12. del()method
# a={1:2,3:4,5:6}
# del a[1]
# print(a)

#13.zip()method
# a=[1,2,3,4]
# b=["ring","nim","love","you"]
# c=dict(zip(a,b))
# print(c)

#14. sorted()method
# orders ={'cappuccino': 54,'latte': 56,'espresso': 72,'americano': 48,'cortado': 41}
# a=sorted(orders.items(), key=lambda x: x[1], reverse=True)
# for i in a:
# 	print(i[0], i[1])