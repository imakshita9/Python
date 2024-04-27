'''Display following menu:  
    1. Add new person name in list.  
    2. Delete a person name    
    ----Accept person name from user.   
    ----Check whether person name exists in the list.    
    ----Confirm for deletion, if user enters y   
    then delete otherwise no. Display appropriate message.  
    '''

list_name=["Akshita","Akansha","Saurabh","Amruta"]

ch=0


print("1.Menu:")
print('''1. Add new person name in list.  
    2. Delete a person name    
    ----Accept person name from user.   
    ----Check whether person name exists in the list.    
    ----Confirm for deletion, if user enters y   
    then delete otherwise no. Display appropriate message. 
     3. Modify persion name for the person   
        ----Accept a person name from user.   
        ----Check whether the person’s name exists.   
        ----If the name exists, Ask for new value and then overwrite the old value.  
    4. Search for the given person’s name.  
    5. Exit
    ''')

# ch=input("Enter the choice:")
while ch !=5:
    ch=int(input("Enter the choice:"))
    if ch==1:
        print(list_name)
        # 1. Add new person name in list. 
        name3=input("Enter the name you want to add: ")
        if name3 in list_name:
            print("Name already exist")
        else:
            list_name.append(name3)
            

        print(list_name)

    elif ch==2:
        print(list_name)
        #  2. Delete a person name 
        name=input("Enter the name you want to delete:")
   
        if name in list_name:
            print(f"{name} is present in list")
            ch_2=input("Do you want to delete the name , type y or n: ")
            if (ch_2=='y'):
                list_name.remove(name)
                print(f"{name} removed")
                print(list_name)
            else:
                print(f"{name} not removed")
                print(list_name)
  
        else:
            print("Name doesn't exist in the list")


    elif ch==3:
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
       
        
# # 4. Search for the given person’s name. 
    elif ch==4:
        name=input("Enter name that you want to search :")
        if name in list_name:
            print(f"{name} exists in a list")
    
    elif ch==5:
        exit(0)

    else:
        print("invalid choice")