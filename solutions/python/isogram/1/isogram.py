def is_isogram(string):
    if len(string) <= 1:
        return True
        
    string = string.casefold()
    allow_char = [' ', '-']
    
    for char in string:
        unique = string.count(char) < 2
        allowed = char in allow_char
        
        if not unique and not allowed:
            return False
     
    return True