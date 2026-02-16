'''
Simple requirements:

Return words that start with input
Empty input → return whole list
No match → empty list
'''

def autocomplete_list(input_word, master_list):
    result = []
    
    for word in master_list:
        if word.startswith(input_word):
            result.append(word)
            
    return result