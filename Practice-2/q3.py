''' 3. Modify persion name for the person   
        ----Accept a person name from user.   
        ----Check whether the person’s name exists.   
        ----If the name exists, Ask for new value and then overwrite the old value.  
    4. Search for person’s name.  
    5. Exit
   '''
list_name=['Isha','Vishaka','Ruhi','Rajat','Rohan']
print(list_name)

ch=0


name=input("Enter name that you want to check :")

if name in list_name:
    print(f"{name} exists in a list")
    if name in list_name:
        a=list_name.index(name)
        b=input("Enter the new name:")
        list_name[a]=b
        print(list_name)
        
else:
    print(f"{name} doesn't exist")

