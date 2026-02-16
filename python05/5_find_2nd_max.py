'''
5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(list):

Test cases: 
1.Empty list → None
2. One element → None
3. Two elements
4. Many elements
5. Shared first place

def test_two_values():
    assert find_2nd_max([1, 5]) == 1

def test_many_values():
    assert find_2nd_max([1, 10, 3]) == 3

def test_shared_first():
    assert find_2nd_max([5, 5, 3]) == 5
'''

def find_2nd_max(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)
    
    if sorted_list[-1] == sorted_list[-2]:
        return sorted_list[-1]
    
    return sorted_list[-2]