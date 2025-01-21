"""
Write a function to check if a string is a palindrome (same forward and backward).
Implement a function to find the maximum element in a list without using the max() function.
Create a dictionary that maps words to their lengths from a list of words.
"""
def is_palindrome(word):
    return word == word[::-1]

def find_max(*args, elements: list = None):
    if not elements and len(args) < 2:
        raise ('Empty List Supplied')
    first_elem = args[0] if args else elements[0]
    element_type = str if isinstance(first_elem, str) else int if isinstance(first_elem, int) else type(first_elem)
    for e in elements:
        if not isinstance(e, element_type):
            raise TypeError(f"Cannot compare between type {type(e)} and {element_type}")
    
    greater = args[0] or elements[0]
    for e in elements:
        if e > greater:
            greater = e
    return greater

def word_to_length(words: list):
    """Maps words from list to a dict of word=length"""
    if not words:
        raise("List must not be empty")
    return {w: len(w) for w in words}

print(find_max(elements=["10, 5", "25", "History", "Z", 'Y']))

print(word_to_length("I really think that Python programming is so cool".split()))