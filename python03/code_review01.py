#Discuss with s team about what you think the output of the code will be.
#1
limit=15
index = 5
while index <=limit:
    print(index)
    index = index + 2;


"""
The index will increase for 2, with start from number 5 and stop by reaching the number 15, 
because we are telling the program that the limit is equal to 15
5
7
9
11
13
15
"""

#2
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i=i+1

#The index will increase for 2, with start from number 5 and stop by number 5
"""
0
1
2
3
4

6
7
8
9
"""

#3.
counter = 0
for i in range(6):
    counter += i
print(counter)
#1 2 3 4 5 6

#4.
x = 0
y = 1

while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y

    print(y)
    print(x)

    y += 1
"""
Start with x = 0, y = 1
Loop while y < 10
If y is even → subtract y from x
Else (if y is odd) → add y*y to x
Increase y by 1 each loop
Print y and x
"""

#5.
message = "its_time_to_get_coding"
print(message[3:7]) # prints _tim those are the index numbers from 3 to 7

#6.
for y in range(1,7):
    s = ""
    for x in range(1,9):
        if x==y:
            s+="#"
        else:
            s+="."
    print(s)
"""
#.......
.#......
..#.....
...#....
....#...
.....#..
"""