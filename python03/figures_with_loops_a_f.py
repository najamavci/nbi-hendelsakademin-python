"""
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
"""
#1)
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)


#2: a-f
for y in range(1,7): #raw number the 7th excluded
    s = ""
    for x in range(1, 9): #loops over the column
        if x == 1:
            s += "#" # put a hash where column number equals row number
        else:
            s += "." #otherwise dot
    print(s)

#3) # on indexes 3, 4, 5 and dots on indexes: 0,1 and 6,7,8

for z in range(1,7):
    d=""
    for t in range(1,9):
        if t in [3, 4, 5]:
            d += "#"
        else:
            d+="."
    print(d)

#4)
rows = 7
columns = 7
for r in range(rows):
    line = ""
    for c in range(columns):
        # Row 3 (index 2) → all #
        if r == 2:
            line += "#"
        # Other rows → # on columns 3,4,5 (indexes 2,3,4)
        elif c in [2,3,4]:
            line += "#"
        else:
            line += "."
    print(line)

#5





