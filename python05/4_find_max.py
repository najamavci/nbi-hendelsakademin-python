'''
4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något

Test cases needed:
Empty list
One number
Many numbers
Negative numbers
Sorted list
Unsorted list


example: 

def find_max(list):

def test_empty():
    assert find_max([]) == None

def test_one_value():
    assert find_max([5]) == 5

def test_many_values():
    assert find_max([1, 10, 3]) == 10

def test_negative():
    assert find_max([-5, -2, -10]) == -2

'''

def find_max(my_list):
    if len(my_list) == 0:
        return None
    
    biggest = my_list[0]
    
    for number in my_list:
        if number > biggest:
            biggest = number
            
    return biggest