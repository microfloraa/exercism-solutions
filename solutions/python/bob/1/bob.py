"""Bob will respond to user input in limited, non-commital ways"""

def response(hey_bob):
    """
    Respond to parameter with a pre-programmed response.

    :param hey_bob: str - user query.    
    """
    if hey_bob == "" or hey_bob.isspace() == True:
        return 'Fine. Be that way!'
    hey_bob = hey_bob.rstrip()
    if hey_bob[-1] == '?' and hey_bob.isupper():
        return 'Calm down, I know what I\'m doing!'
    if hey_bob[-1] == '?':
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    return "Whatever."
        
    
