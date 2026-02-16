'''
Test cases:

Empty list → True
One number → True
Sorted list → True
Unsorted list → False
Equal numbers → True
'''

def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True