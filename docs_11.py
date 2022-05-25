# Q19. Write a Python program to remove duplicates from Dictionary.
# from turtle import update


a= {'id1': 
  {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
  },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
  },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
  },
}
# b={}
# for key,value in a.items():
#     if value not in b.values():
#         b[key]=value
# print(b)
b={}
for key,value in a.items():
    if value not in b.values():
        b[key] = value
print(b)       
