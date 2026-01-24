'''
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:

Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!
Version 2: programmet ska tala om ifall det blev oavgjort.

'''
teamTottenham = int(input("How many goals had Tottenham "))
teamLiverpool = int(input("How many goals had Liverpool "))

if teamTottenham == teamLiverpool:
    print("Both team had equal number of goals! ")
elif teamTottenham < teamLiverpool:
    print("Liverpool won!")
elif teamLiverpool < teamTottenham:
    print("Tottenham won!")