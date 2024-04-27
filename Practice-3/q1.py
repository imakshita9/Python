'''.create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and 
second last char of s2, 
and so on. Any leftover chars go at the end of the result.
Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX'''

s1="Abc"
s2="Xyz"

len_1=len(s1)
len_2=len(s2)


# s3=s1[0]+s2[-1]+s1[1]+s2[-2]+s1[-1]+s2[0]
# print(s3)

max_1=max(len_1,len_2)
s3=""
print(max_1)
for i in range(max_1):
    if i < len_1:
        s3=s3 + s1[i] 
    if i < len_2:
        s3=s3 + s2[-(i+1)]

print(s3)
