'''practice List functions. 
 
					
                    	a) add at last position  
						b) add at given position  
						
						2. Delete data by value   
						 
						3. delete data by position  
						4. delete last element  
						5. delete from particular position  
						6. sort  a) ascending  b) descending  
						5. reverse  
						6. Print in sorted order without changing original list  
						7. print in reverse order without changing original list  
						'''

list1=["ELP","C&DS","DBMS","F-IOT","MICROCONTROLLER","WEB-DEV"]
print(list1)
list1.append("JAVA") #a) add at last position 
print(list1)

#add at given position  
list1[2]="CLOUD"
print(list1)

#Delete data by value
list1.remove("F-IOT")
print(list1)

#Delete data by position  
del list1[1]
print(list1)

# delete last element  
del list1[-1]
print(list1)


# sort  a) ascending  b) descending  
# 						5. reverse  

list1.sort()
print("Sorted list is: ",list1)
print("Ascending order of list is: ",list1)

list1.sort(reverse=True)
print("Descending list is: ",list1)



# Print in sorted order without changing original list  
list2=sorted(list1)
print(list2)
print(list1)
# print in reverse order without changing original list
list2=sorted(list1,reverse=True)
print(list2)





