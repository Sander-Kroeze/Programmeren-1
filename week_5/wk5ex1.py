# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam: Sander Kroeze en Chris Wibbelink
# Probleemomschrijving: conversie binair <-> decimaal


def is_odd(n):
    """
    Kijkt of het getal oneven is
    """
    if n % 2:
        return True
    else:
        return False

assert not is_odd(42)
assert is_odd(43)


def num_to_binary(n):
    """
    Krijgt een cijfer mee en transvormeerd deze naar binary code
    """
    if n == 0:
        return ''
    elif n % 2 == 1:
        return num_to_binary(n // 2) + '1'
    else:
        return num_to_binary(n // 2) + '0'

def binary_to_num(s):
    """
    krijgt een binary string als input
    veranderd deze naar een cijfer
    """
    if s == "":
        return 0
    return binary_to_num(s[:-1]) * 2 + (s[-1] == '1')

def increment(s):
    n = int(s)
    x = n + 1
    r = num_to_binary(x)
    if "0" not in s:
        return "0" * len(s)
    return  r