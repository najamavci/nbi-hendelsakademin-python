'''
1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.

Equivalence classes for degree:

degree < -273.15 → invalid
degree = -273.15
degree > -273.15
'''

def test_below_absolute_zero():
    assert c_to_f(-300) == None

def test_absolute_zero():
    assert c_to_f(-273.15) == -459.67

def test_normal_temp():
    assert c_to_f(0) == 32
