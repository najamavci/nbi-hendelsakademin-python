#1)
rows = 6
columns = 7

for r in range(rows):
    line = ""
    for c in range(columns):
        # Alternate between # and .
        if c % 2 == 0:
            line += "#"
        else:
            line += "."
    print(line)
print("\n")

#2)
rows = 6
columns = 7

for r in range(rows):
    line = ""
    for c in range(columns):
        # Top and bottom borders
        if r == 1 or r == 4:
            if 1 <= c <= 5:
                line += "#"
            else:
                line += "."
        # Sides of the box
        elif r in [2, 3]:
            if c == 1 or c == 5:
                line += "#"
            else:
                line += "."
        # Empty rows
        else:
            line += "."
    print(line)

print("\n")

