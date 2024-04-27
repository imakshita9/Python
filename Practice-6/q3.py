'''
Create a file productdata.txt, using notepad and add contents in following format using python script.
Id:name:description:category:price
For example
123:lays:very crispy:chips:40
124:Good day:very sweet:biscuits:35
125:maggi:yummy:snacks:60
225:chings:yummy:snacks:65
123:nachos:very crispy:chips:120'''

with open("productdata.txt","w") as f:
    f.write("123:lays:very crispy:chips:40"+"\n")
    f.write("124:Good day:very sweet:biscuits:35"+"\n")
    f.write("125:maggi:yummy:snacks:60"+"\n")
    f.write("225:chings:yummy:snacks:65"+"\n")
    f.write("123:nachos:very crispy:chips:120"+"\n")