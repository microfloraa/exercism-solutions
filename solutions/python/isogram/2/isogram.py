def is_isogram(string):
    scrubbed = [char.casefold() for char in string if char.isalpha()]
    return len(scrubbed) == len(set(scrubbed))