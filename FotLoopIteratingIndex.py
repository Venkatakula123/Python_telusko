my_list = [3, 5, 6, 8, 4]  
for iter_var in range( len( my_list ) ): # Here instead of list values used index values only 
    my_list.append(my_list[iter_var] + 2)  
    print( my_list )  