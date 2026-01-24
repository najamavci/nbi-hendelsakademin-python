'''
5 Miniräknare
1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)
2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.
3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.
4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)
För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

'''# Ask the user for three numbers
t1 = float(input("Enter number 1: "))
t2 = float(input("Enter number 2: "))
t3 = float(input("Enter number 3: "))

# 1. Calculate the sum
total = t1 + t2 + t3
print("Sum:", total)

# 2. Find the largest number (without using max)
if t1 >= t2 and t1 >= t3:
    largest = t1
elif t2 >= t1 and t2 >= t3:
    largest = t2
else:
    largest = t3

print("Largest number:", largest)

# 3. Check if numbers are equal
if t1 == t2 == t3:
    print("Three equal? yes")
    print("Two equal? yes")
elif t1 == t2 or t1 == t3 or t2 == t3:
    print("Three equal? no")
    print("Two equal? yes")
else:
    print("Three equal? no")
    print("Two equal? no")

# 4. Find the middle number
# A middle number exists only if all three are different or all three are equal
if t1 == t2 == t3:
    print("Middle number:", t1)
elif t1 != t2 and t1 != t3 and t2 != t3:
    if (t1 > t2 and t1 < t3) or (t1 < t2 and t1 > t3):
        print("Middle number:", t1)
    elif (t2 > t1 and t2 < t3) or (t2 < t1 and t2 > t3):
        print("Middle number:", t2)
    else:
        print("Middle number:", t3)
else:
    print("Middle number: does not exist")
