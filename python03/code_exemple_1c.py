#Skriv om 1b så att den använder en while-loop.
"""
answer= 0;
for i in range(1,101):
    answer +=i
print(answer)
"""
answer=0;
x=1
y=100
while x <=y:
    answer+=x
    x+=1 #is exactly the same as: x = x + 1
    print(answer)
# output is 5050
"""
Condition: x <= y → 1 <= 100 
answer += x → 0 + 1 = 1
x += 1 → x becomes 2
Print → 1
"""