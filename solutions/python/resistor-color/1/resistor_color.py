def color_code(color):
    color_num = {'black': 0, 
                 'brown': 1, 
                 'red': 2, 
                 'orange': 3, 
                 'yellow': 4, 
                 'green': 5, 
                 'blue': 6, 
                 'violet': 7, 
                 'grey': 8, 
                 'white': 9}
    return color_num.get(color)

def colors():
    color_num = {'black': 0, 
                 'brown': 1, 
                 'red': 2, 
                 'orange': 3, 
                 'yellow': 4, 
                 'green': 5, 
                 'blue': 6, 
                 'violet': 7, 
                 'grey': 8, 
                 'white': 9}
    return list(color_num.keys())