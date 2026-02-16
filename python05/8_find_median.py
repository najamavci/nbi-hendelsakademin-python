'''

Test cases:

Empty list → None
Odd number of elements
Even number of elements
Unsorted list

'''
def find_median(numbers):
    if len(numbers) == 0:
        return None
    
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    
    middle = length // 2
    
    if length % 2 == 1:
        return sorted_list[middle]
    else:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2