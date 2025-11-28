CODE = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

def value(colors):
    digits = [CODE.index(color) for color in colors[:2]]
    accum = 0
    
    for digit in digits:
        accum = accum * 10 + digit
    return accum