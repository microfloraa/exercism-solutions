def value(colors):
    code = [
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

    first_two = [code.index(color) for color in colors[:2]]
    return int(''.join(map(str, first_two)))