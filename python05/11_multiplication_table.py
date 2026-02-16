'''
test: 

def test_table():
    assert multiplication_table(3, 4) == [3, 6, 9, 12]
'''

def multiplication_table(n, limit):
    result = []
    
    for i in range(1, limit + 1):
        result.append(n * i)
        
    return result