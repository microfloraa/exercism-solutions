"""Bob will respond to user input in limited, non-commital ways"""


def response(hey_bob):
    """
    Respond to parameter with a pre-programmed response.

    :param hey_bob: str - user query.    
    """
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    capital_bob = hey_bob.isupper()
    question_bob = hey_bob.endswith('?')
    if capital_bob and question_bob:
        return 'Calm down, I know what I\'m doing!'
    if capital_bob:
        return 'Whoa, chill out!'
    if question_bob:
        return 'Sure.'
    return "Whatever."
        
    
