def is_leap_year(a_year):
    """Return true or false whether a given year is a leap year."""
    if (a_year) % 2 == 0:
        if (a_year) % 4 == 0 or (a_year) % 400 == 0:
            print(True)
        else: 
            print(False)
    else:
        print(False)
    
is_leap_year(2002)