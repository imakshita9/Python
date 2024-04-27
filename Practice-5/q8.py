'''Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. For example, translate("this
is fun") should return the string "tothohisos isos fofunon".'''


vowels=('a','e','i','o','u')
space=(" ")

translate = 'this is function'

for i in translate :
    if i in space :
        print(i,end='')
    
    elif i not in vowels :
        print(f"{i}o{i}",end='')
    else:
        print(f"{i}",end="")

print("")

