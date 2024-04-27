'''Write a program to find out whether a student is pass or fail. it requires a total of 40% 
and at least 33% in each subject to pass.
 Assume 3 subjects and take marks as an input from the user.'''

marks1=int(input("Enter marks of Maths subject out of 100: "))
marks2=int(input("Enter marks of English subject out of 100: "))
marks3=int(input("Enter marks of Science subject out of 100: "))
total=marks1+marks2+marks3
percent=(total/300)*100

per_sub1=(marks1/100)*100
per_sub2=(marks2/100)*100
per_sub3=(marks3/100)*100

if percent > 40 and per_sub1 > 33 and per_sub2>33 and per_sub3 > 33:
    print("Student is passed")
else:
    print("Student is fail")