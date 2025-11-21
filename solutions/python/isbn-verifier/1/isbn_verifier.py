def is_valid(isbn):
    isbn_list = []
    valid_char = list('0123456789X-')

    if 'X' in isbn[:-1]:
        return False
    
    for char in isbn:
        if char not in valid_char:
            return False
        if char == '-':
            continue
        if char == 'X':
            char = '10'
        isbn_list.append(int(char))

    if len(isbn_list) != 10:
        return False

    check_digit = []
    multiplier = 10
    
    for digit in isbn_list:
        product = digit * multiplier
        check_digit.append(product)
        multiplier -= 1

    if sum(check_digit) % 11 != 0:
        return False
    return True