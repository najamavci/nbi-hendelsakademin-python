'''
Requirements:

Empty string → 0
One word → 1
Multiple words → correct number
'''

def count_words(sentence):
    if sentence == "":
        return 0
    
    words = sentence.split()
    return len(words)