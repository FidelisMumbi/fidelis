#create a list named my_list
my_list=[]

#appending values to from values to my_list
values=[10,20,30,40]


for val in values:
    my_list.append(val)
    
#confirming that now my_list==values
print(f'my_list after appending values:\nmy_list={my_list}\n')
 
#inserting val 15 at second position in list
position = 2
value_to_insert= 15
 
my_list.insert(position,value_to_insert)
 
print(f'value 15 appended to my_list at index 3\n{my_list}\n')
 
#extend my_list with another list x_list
x_list=[50,60,70]
my_list.extend(x_list)
 
print(f'extended list:\n{my_list}\n')
 
 #remove the last element from the list
my_list.pop(-1)
 
print(f'last item has been released from my_list\n{my_list}\n')
 
#sort my_list in ascending order
#filter for all the minimal values appending to the new list
#then removing the value from the old list ensuring its not found again
asc_list=[]
 
for v in my_list:
     minimal=min(my_list)
     asc_list.append(minimal)
     my_list.remove(minimal)
     
#reassignment of asc back to my_list
my_list=asc_list    
 
print(f'ascending list;\n{my_list}\n')
 
#find the value in my_list 
for n in my_list:
     if int(n) == 30:
        print(f'index of 30 in my_list:\n{my_list.index(30)}\n')
     else:
        pass
