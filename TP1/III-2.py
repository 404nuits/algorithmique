
def ask_number(msg, min, max):
    """Ask user for a number between two numbers (included)

    Args:
        msg (str): Message to input to the user
        min (int): Minimal number
        max (int): Maximal number
    """
    
    # Initialize rep out of the bounds
    rep = min-1
    
    while (rep < min or rep > max):
        
        rep = int(input(msg))
        
    return rep

if __name__ == '__main__':
    
    day = ask_number('Entrez votre jour de naissance : ', 1, 31)
    month = ask_number('Entrez votre mois de naissance : ', 1, 12)
    year = ask_number('Entrez votre année de naissance : ', 1900, 2100)
    print(f'{day:02d}/{month:02d}/{year}')
