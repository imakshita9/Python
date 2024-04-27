'''>.2. Given two strings, s1 and s2, create a new string by appending s2 in 
the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt'''

s2="Isha"
s1="Akshita"
len=len(s1)
print(len)

mid=int(len/2)
s3=s1[:mid]+s2+s1[mid:]
print(s3)
# print(mid)

# print(s1+s2)
