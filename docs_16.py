# Q27.Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# Sample input if key is id: then 6

student =[{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# for i in student:
#     if i['success']==True:
#         c=c+1
# print(c)
   
print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student)) 