'''111,Anamika decorators,30,200000
222,Shree designs,45,300000
333,saidatta arts,50,400000
112,Anu decorators,30,100000
212,Shertree designs,35,500000
313,datta arts,50,400000
121,Raj decorators,30,200000
232,Shreyas designs,45,300000
353,sai,50,400000

Save as decorators.txt.
a.	Assign headings (id ,movie,shows,collections) to respective columns
b.	Display first 3 lines of the file.
c.      Display last 3 lines of the file.
c.	Display only movie name and collection columns
d.	Draw a bar graph using moviname and no of shows'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#@Assign headings (id ,movie,shows,collections) to respective columns
fd=pd.read_csv("decorators.txt", names=['id' ,'movie','shows','collections'])
print(fd)
print("\n")

#b.	Display first 3 lines of the file.
print(fd.head(3))
print("\n")

# Display last 3 lines of the file.
print(fd.tail(3))
print("\n")

#Display only movie name and collection columns
print(fd[["movie","collections"]])
print('\n')

# Draw a bar graph using moviname and no of shows
fd.plot(x="movie" , y="shows" , kind="bar")
plt.xlabel("Movies")
plt.ylabel("No. of Shows")
plt.show()