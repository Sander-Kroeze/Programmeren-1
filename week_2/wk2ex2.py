# Gemaakt door Sander en Chris
# Klas ITV1K

from math import *

def dbl(x):
    """Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 2 * x

def tpl(x):
    """Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 3 * x  

def sq(x):
    """Geeft het kwadraat van het argument terug
    """

    return x ** x

def interp(low, hi, fraction):
    """
    """
    
    return (hi - low) * fraction + low

def flipside(s):
    """Flipside: deelt de woorden door 2 en keert ze om.
    """
    x = len(s) // 2

    return s[x:] + s[:x]

def checkend(s):
    """Kijkt naar het eerste letter en de laatste, vergelijkt deze en geeft aan of ze gelijk zijn of niet
    """

    x = s[0]
    y = s[-1]

    if x == y:
        return True 
    else:
        return False

def convert_from_seconds(s):
    """Put your docstring here
    """
    days = s // (24 * 3600)  #Het aantal dagen
    time = s % (24 * 3600)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return [days, hours, minutes, seconds]

