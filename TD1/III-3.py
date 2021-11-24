
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
        rep = int(input(msg+f', compris entre {min} et {max} : '))
        
    return rep

def is_leap_year(year):
    """Check if a year is a leap year
    Based on rules found here :
    https://fr.wikipedia.org/wiki/Ann%C3%A9e_bissextile#R%C3%A8gle_actuelle


    Args:
        year (int)

    Returns:
        bool: True if year is a leap year, False else
    """
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))



if __name__ == '__main__':
    
    ok = False
       
    while(not ok):
        day = ask_number('Entrez votre jour de naissance', 1, 31)

        month = ask_number('Entrez votre mois de naissance', 1, 12)

        if (month == 2):
        # February
            if (day>29):
                print('Erreur : Le jour est supérieur à 29 alors que nous sommes en février')
                continue

        elif (month in [4,6,9,11]):
        # 30 days months
            if (day>30):
                print('Erreur : Le jour est supérieur à 30')
                continue
            
            
        year = ask_number('Entrez votre année de naissance', 1900, 2100)

        if (not is_leap_year(year)):
            if (day>28 and month==2):
                print('Erreur : L\'année n\'est pas bissextile')
                continue
            
        ok = True


    print(f'{day:02d}/{month:02d}/{year}')
