# Programmeren I, opgave 2
# Bestandsnaam: wk4ex2.py
# Naam: Sander en Chris
# Probleemomschrijving: Caesar 

# def encipher(text, s, result=''): 

#     if len(text) == 0:
#         return result
#     elif "a" <= text[0] <= "z":
#         if ord(text[0]) + s <= ord("z"):
#             return encipher(text[1:], s, result + chr((ord(text[0]) + s - 97) % 26 + 97) ) 
#     elif (text[0].isupper()):
#         if ord(text[0]) + s <= ord("Z"):
#             return encipher(text[1:], s, result + chr((ord(text[0]) + s - 65) % 26 + 65))

def rot(c, n):
    if 'a' <= c <= 'z':
        if ord(c) + n <= ord("z"):
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)
    elif "A" <= c <= "Z":
        if ord(c) + n <= ord("Z"):
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)
    else:
        return c

def encipher(s, n):
# Kijkt kijkt naar de lengte van s, bij elke loop wordt 1 letter doorgespeelt naar rot en doorgedraait met n
    L = [rot(s[x], n) for x in range(len(s))]

# zorgt er voor dat alles in 1 string komt te staan
    string = ''.join(L)

    return string

assert encipher("xyza", 1) == "yzab"
assert encipher("Z A", 1) == "A B"


def decipher(s):
    """
    Krijg een enchipherd string binnen en decipherd deze
    Deze functie maakt gebruik van rot2 en letter_prob
    """
# kijkt wat de lengte is van s, en krijgt een range van 26 mee, de functie rot wordt aangeroepen met een getal van range(26 en van range(leng(s)))
    L = [sum([rot2(s[n], x) for n in range(len(s))]) for x in range(26)]

# Kijkt naar de locatie van het hoogste getal wat hij terug krijgt in de lijst L
    x = L.index(max(L))

# vertaald alle chars met de functie rot, deze krijg als input de range van de lengte van s en de key x
    lists = [rot(s[p], x) for p in range(len(s))]

# zorgt er voor dat alles in 1 string komt te staan
    string = ''.join(lists)

# geeft het resultaat weer
    return string

def rot2(c, n):
    """
    krijgt een char mee en een getal, dan kijkt hij wat het char is na zoveel rotaties
    en geeft het nieuwe char terug
    """
    if 'a' <= c <= 'z':
        if ord(c) + n <= ord("z"):
            return letter_prob(chr(ord(c) + n))
        else:
            return letter_prob(chr(ord(c) + n - 26))
    elif "A" <= c <= "Z":
        if ord(c) + n <= ord("Z"):
            return letter_prob(chr(ord(c) + n))
        else:
            return letter_prob(chr(ord(c) + n - 26))
    else:
        return letter_prob(c)


def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0


def blsort(L):
    """
    sorteert een lijst die binnen komt op binary getallen
    """
    j = -1
    L2 = [0,1]
    # controleerd of i in L2 zit, als dit niet zo is geeft hij hem niet terug in de lijst
    binaryTest = [i for i in L if i in L2]

    for i in range(len(binaryTest)): 
        # als het nummer kleiner is dan 1, wissel je het om met j- nummer
        if L[i] < 1: 
            j = j + 1 
            print(j)
            # wisselt plekken van 0 om 
            binaryTest[i], binaryTest[j] = binaryTest[j], binaryTest[i] 
    return binaryTest

def gensort(L):
    """"
    deze functie sorteert de lijst L via recursie
    """
    if len(L) <= 1:
        return L
    else:
        # hier vind de recursie plaats, als e kleiner is dan het eerste getal in de lijst
        return gensort([e for e in L[1:] if e <= L[0]]) + [L[0]] + gensort([e for e in L[1:] if e > L[0]])

def lingo(s, t):
    """"
    De lingo funcite, deze funcite kijkt of elk letter van s in t voor komt, als dit zo is komt er 1 punt bij
    als dit niet zo is niet
    """
    j = 0
    if not s or not t:
        return 0

    return [j + 1 for i in range(len(s)) if s[i] in t]

def exact_change(target_amount, L ):
    """
    De exact change functie geeft true terug als je het ingevoerde bedrag exact kan betalen
    als dit niet het geval is krijg je false terug
    """
    if target_amount > sum(L):
        return False
    elif target_amount == 0:
        return True
    elif target_amount < 0:
        return False
    elif target_amount > 0 and not L:
        return False
    else:
        loseit = exact_change(target_amount, L[1:])
        useit = exact_change(target_amount - L[0], L[1:])
        return loseit or useit

def lcs(s, t):
    if not s or not t:
        return ''
    if s[0] is t[0]:
        return s[0] + lcs(s[1:], t[1:])
    result1 = lcs(s[1:], t)
    result2 = lcs(s, t[1:])
    if len(result1) > len(result2):
        return result1
    else:
        return result2

    






    




