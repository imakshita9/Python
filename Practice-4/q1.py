'''Ask user if they want to continue to accept multiple values.

Write a program to accept name of a person and their vehicle and store it in a dictionary

Display following menu:

1. Add new person name and a vehicle name. 
	-Accept person name from user.
	-Check whether person name exists in the dictionary. -If does not exist,add data.
2. Delete a person name and vehicle name from the dictionary.

-Accept person name from user.

-Check whether person name exists in the dictionary. -If exists show person name and vehicle name to the user. -Confirm for deletion, if user enters y

then delete otherwise no. Display appropriate message.

3. Modify vehicle name for the person ---Accept a person name from user.

-Check whether the person's name exists.

If the name exists, show the person's name and vehicle name to user.

Ask for new value and then overwrite the old value.


4. Search list of people, who have given a vehicle
	---Accept a vehicle name and print all persons name who have that vehicle.

5. Search vehicle for the given person's name.
	-Accept person name and print his vehicle.if person not found display msg.


6. Display all person names. 

7. Display all vehicle names.

9. Display Dictionary

10 Exit'''

dict_1={}
ch=0
print('''Menu:
      1.Add new person and add new vehicle
      2.Delete person and vehicle name
      3. Modify vehicle name for the person ---Accept a person name from user
      4.Search list of people, who have given a vehicle
      5.Search vehicle for the given person's name.
      6.Display all person names
      7.Display all vehicle names.
      8. Display Dictionary
      9.Exit''')


while True:
    ch=int(input('Enter your choice:'))
    if (ch == 1):
        person=input("Enter name of person:")
        
        if person in dict_1.keys():
            print("Name already exist")
        else:
            # dict_1[person]
            vehicle=input("Enter vehicle name:")
            dict_1[person]=vehicle
            
        print(dict_1)
    
    elif ch==2:
        print(dict_1)
        #  2. Delete a person name 
        person=input("Enter the name you want to delete:")
   
        if person in dict_1.keys():
            print(f"{person} is present in list")
            ch_2=input("Do you want to delete the name , type y or n: ")
            if (ch_2=='y'):
                del dict_1[person]
                print(f"{person} removed")
                print(dict_1)
            else:
                print(f"{person} not removed")
                print(dict_1)
        else:
            print("Name doesn't exist in dictionary")    


    elif ch==3:
        person=input("Enter name that you want to check :")
        if person in dict_1.keys():
            print(f"{person} exists in a list")
            print(dict_1)

            if person in dict_1.keys():
                b=input("Enter the new vehicle:")
                dict_1[person]=b
            print(dict_1)
                
        else:
            print(f"{person} doesn't exist")


    elif ch == 4:
        count=0
        print(dict_1)
        vehicle=input("Enter the vehicle name that you want to search: ")
        for key,value in dict_1.items():
            if dict_1[key] == vehicle:
                print("person:", key , " vehicle:", vehicle)
                # print("vehicle: ",vehicle)
            # else:
            #     print(f"{vehicle} not present")
         
                count=+1

        if count == 0:
            print(f"{vehicle} not present")


    elif ch == 5:
        count=0
        print(dict_1)
        person=input("Enter the person name that you want to search: ")
        if person in dict_1.keys():
            print("person:", person , " vehicle:", vehicle)
        else:
            print(f"{person} not present")


    elif ch == 6:
        print("person names in dictionary:")
        for person in dict_1.keys():
            print(person)

    elif ch == 7:
        print("vehicle names in dictionary:")
        for vehicle in dict_1.values():
            print(vehicle)

    elif ch == 8:
        print(dict_1)

    elif ch == 9:
        exit(0)
    

       
