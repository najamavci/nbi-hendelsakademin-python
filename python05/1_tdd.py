'''
Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

1b Vilka ekvivalensklasser har parametern degree?

1c Skriv ett testfall.

----------------


#1a. x > 100

#Ekvivalensklasser:

#x ≤ 100

x > 100

-----------------

1b. y == 42

y = 42

y ≠ 42
-------------------

#1c. len(text) >= 5

längd < 5
längd ≥ 5

--------------

#1d. z == True

z är True

z är False

#(om vi är noga: z är något annat än bool)

-----------

#1e. 8 < v < 16
#v ≤ 8

8 < v < 16

v ≥ 16
------------

#1f. w == 32 or w == 64 or w == 128

w = 32

w = 64

w = 128

#w är något annat

#1g.
if x < 5
elif x < 10
elif x < 15
else

#Ekvivalensklasser:

x < 5
5 ≤ x < 10

10 ≤ x < 15

x ≥ 15

'''