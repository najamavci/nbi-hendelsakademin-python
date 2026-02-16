'''
2 Det har smugit sig in kommentarer i stället för kod på några ställen. Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = # ???
    actual   = # ???
    assert actual == expected
    
def test_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5
    assert # ???
    assert # ???


def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert actual == expected

 def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1, 2]) == 3
    assert sum_list([1, 2, 3, 4, 5]) == 15

'''

def sum_list(my_list):
    total = 0
    for number in my_list:
        total = total + number
    return total

