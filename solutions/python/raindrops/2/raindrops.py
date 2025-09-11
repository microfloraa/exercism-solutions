"""Function to convert a number to raindrop noises."""

def convert(number):
    """Convert a number to raindrop noises.
    
    :param number: int - number to convert.
    :result: str - raindrop noises.
    """
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    
    results = (sound for divisor, sound in sounds.items() 
               if number % divisor == 0)
    
    return ''.join(results) or str(number)