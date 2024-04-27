'''Print following pattern. (use two loop only)
#
##
###
####
#####
######
#####
####
###
##
#'''

row=7
pattern=""
for i in range(1,row+1):
    pattern += "#"
    print(pattern)

pattern=""
for i in range(-6,0):
    pattern = -i * "#"
    print(pattern)


