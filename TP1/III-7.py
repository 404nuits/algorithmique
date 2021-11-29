
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


def ask_date():
    """Ask user for a date until it's a correct date

    Returns:
        list: list of [day, month, year]
    """
    
    ok = False
       
    while(not ok):
        day = ask_number('Entrez le jour', 1, 31)

        month = ask_number('Entrez le mois', 1, 12)

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
            
            
        year = ask_number('Entrez l\'année', 1900, 2100)

        if (not is_leap_year(year)):
            if (day>28 and month==2):
                print('Erreur : L\'année n\'est pas bissextile')
                continue
            
        ok = True

    return [day,month,year]
    
def next_date(day,month,year):
    """Returns the day coming after day entered in parameters

    Args:
        day (int): day between 1 and 31
        month (int): month between 1 and 12
        year (int): year between 1900 and 2100

    Returns:
        list: list of [day, month, year]
    """

    if (day == 31) or (day == 30 and month in [4,6,9,11]) or (day == 29 and month == 2) or (day == 28 and month == 2 and not is_leap_year(year)):
    # If any if these is true, we are the last day of the month (31th day or 30 days month or february (leap year or not))
        if (month == 12):
            year+=1
            
            # Init to first month of year
            month=1
        else:
            month+=1
            
        # Init to first day of month
        day=1
    else:
        day+=1
    return [day,month,year]

def number_of_days(start_date, end_date):
    """Get number of days between two dates
    Pre : end_date must be after start_date

    Args:
        start_date (list): list of [day, month, year]
        end_date (list): list of [day, month, year]

    Returns:
        int: Number of days between two dates
    """

    current_date = start_date
    n_days = 0
    
    # We start at the start date and we go day by day, incrementing each time until we reach the end date
    while (current_date != end_date):
        current_date = next_date(current_date[0], current_date[1], current_date[2])
        n_days+=1
        
    return n_days

def age(birth_date, today_date):
    """Get someone's age between its birth date and another date

    Args:
        birth_date (list): list of [day, month, year]
        today_date (list): list of [day, month, year]

    Returns:
        int: someone's age
    """

    age = today_date[2] - birth_date[2]
    if (today_date[1] < birth_date[1]) or (today_date[1] == birth_date[1] and today_date[0] < birth_date[0]):
        age-=1
    return age

def print_date(day,month,year):
    print(f'{day:02d}/{month:02d}/{year}')
    
if __name__ == '__main__':
    
    print('Date de naissance :')
    birth_day,birth_month,birth_year = ask_date()
    print_date(birth_day,birth_month,birth_year)
    
    print('\n\nDate du jour :')
    today_day,today_month,today_year = ask_date()
    print_date(today_day,today_month,today_year)
    
    print('\n\nDate de demain : ')
    tomorrow_day,tomorrow_month,tomorrow_year = next_date(today_day, today_month, today_year)
    print_date(tomorrow_day,tomorrow_month,tomorrow_year)
    
    n_days = number_of_days([birth_day,birth_month,birth_year], [today_day, today_month, today_year])
    print(f'\n\nNombre de jour entre la date de naissance et aujourd\'hui : {n_days}')
    
    age = age([birth_day,birth_month,birth_year], [today_day, today_month, today_year])
    if age>1:
        print(f'\n\nVous avez {age} ans')
    else:
        print(f'\n\nVous avez {age} an')