def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    return all(char in sentence.casefold() for char in alphabet)
