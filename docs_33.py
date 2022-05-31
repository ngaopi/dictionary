# Q33.Python: Print a dictionary line by line
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 

students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for x in students:
    print(x)
    for y in students[x]:
        print(y,":",students[x][y])
        