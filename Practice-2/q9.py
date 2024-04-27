'''
> 3.two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan '''

s1="America"
s2="Japan"
print(s1)
print(s2)
s_1=len(s1)
mid_1=int(len(s1)/2)
print(s1[mid_1])

s_2=len(s2)
mid_2=int(len(s2)/2)

s3=s1[0] + s2[0] + s1[mid_1] + s2[mid_2] + s1[-1] + s2[-1]
print(s3)