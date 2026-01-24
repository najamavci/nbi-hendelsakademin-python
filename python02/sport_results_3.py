'''
Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.
'''

teamTottenham = int(input("How many goals had Tottenham "))
teamLiverpool = int(input("How many goals had Liverpool "))
if teamTottenham == teamLiverpool:
    print("Both team had equal number of goals! ")
elif teamTottenham < teamLiverpool:
    print("Liverpool won with " + str(teamLiverpool) + " goals!")
elif teamLiverpool < teamTottenham:
    print("Tottenham won with " + str(teamTottenham) + " goals!")