'''
3a Diskutera följande kod. Ett testfall räcker inte för att testa funktionen - föreslå fler testfall, som täcker in alla olika möjligheter för count_vowels.
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

test:

No vowels
One vowel
Many vowels
Same vowel multiple times
Uppercase letters
Mixed characters

#examples: 

def test_one_vowel():
    assert count_vowels("a") == 1

def test_many_vowels():
    assert count_vowels("aeiou") == 5

def test_same_vowel_many_times():
    assert count_vowels("aaa") == 3

def test_uppercase():
    assert count_vowels("AEIOU") == 5

def test_mixed():
    assert count_vowels("Hello World") == 3
'''

def count_vowels(word):
    vowels = "aeiouyåäö"
    count = 0
    
    for letter in word.lower():
        if letter in vowels:
            count = count + 1
            
    return count
