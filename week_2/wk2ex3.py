# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam: Sander en Chris
# Problemomschrijving: Feest met functies!




#
# voorbeeldfunctie leng uit het college
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])


# 
# Zelfgemaakte opgaven
# 
def mult(n, m):
    """Doet de ingevoerde waarde keer elkaar
    """
    if m < 0:
        return -mult(n, -m)
    elif m == 0:
        return 0
    elif m == 1:
        return n
    else:
        return n + mult(n, m - 1)

def dot(l, k):
    """ krijgt als input 2 lijsten met getallen, de lijsten moeten even lang zijn
        anders werkt het niet en krijg je '0' terug
    """
    
    if len(k) == 0 or len(l) == 0:
        return 0.0
    elif len(k) == len(l):
        vermeenigvuldig =  dot(l[1:], k[1:]) + mult(l[0],k[0])               
        return vermeenigvuldig

def ind(e, L):
    if e in L:
        if L == []:
            return -1
        elif L[0] == e:
            return 0
        re = ind(e, L[1:])
        if re < 0:
            return re
        return re + 1
    elif e not in L:
        return leng(L)


def letter_score(let):
    """ laat de score per letter zien
    """

    if let == '':
        return 0

    if let in 'adeinorst':
        return 1
    elif let in 'ghl':
        return 2
    elif let in 'bcmp':
        return 3
    elif let in 'jkuvw':
        return 4
    elif let in 'f':
        return 5
    elif let in 'z':
        return 6
    elif let in 'xy':
        return 8
    elif let in 'q':
        return 10 
    else:   
        return 0

def scrabble_score(s):  
    """ Met deze functie kun je woorden invoeren en daarvoor punten krijgen via de functie die hierboven staat.
    """

    return letter_score(s[0]) + scrabble_score(s[1:])

def one_dna_to_rna(c):
    """Converts a single-character c from DNA nucleotide
       to complementary RNA nucleotide
    """

    if 'A' in c:
        return 'U'
    elif 'C' in c:
        return 'G'
    elif 'G' in c:
        return 'C'
    elif 'T' in c:
        return 'A'
    else:
        return ""  

def transcribe(s):
    """ maakt gebruik van de functie "one_dna_to_rna" en zet de input om
    """

    if s == '':
        return ''
    elif s[0] in 'ACGT':
        ans = one_dna_to_rna(s[0]) + transcribe(s[1:])
        return ans
    else:
        return transcribe(s[1:])
    


    