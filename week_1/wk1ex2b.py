"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 0.0

    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten!")
    print()

    flavor = input("Welke smaak zoekt u? ")
    if flavor == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif flavor == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    else:
        print("Ieder zijn smaak...")
    print()
# Nieuwe kaas keuze met if, elif en else 
    cheese = input("wilt u gesmolten kaas of normale kaas? [gesmolten/normale]")
    if cheese == "gesmolten":
        print("Gesmolten kaas is een goeie keuze... maar wat heb je er aan...")
        print("Misschien had je toch iets anders moeten kiezen...")
    elif cheese == "normale":
            print("Normale kaas kan ook lekker zijn... maar persoonlijk heb ik liever ham er nog bij..")
    else:
        print("Heb je wel goed geluisterd? Het maakt ook niet uit.. ik kom hier later wel op terug...")
    print()
# Nieuwe wapen keuze met if 2x elif en else
    weapon = input("Nou moet je jezelf beschermen onderweg als je gevaar tegen komt, wat mag het zijn? [zwaard/bijl/mes]")
    if weapon == 'zwaard':
        print('Met een zwaard zit je altijd goed... of toch niet? Een zwaard is wel groot en zwaar natuurlijk.')
    elif weapon == 'bijl':
        print('Een bijl dus.. Goede keuze! Dit wapen is makkelijk te gebruiken en mee te nemen, zou dit wapen ook nog iets anders kunnen?')
    elif weapon == 'mes':
        print('Kies je echt voor dit wapen? ... Oke dan, hopen dat je de gevaren onderweg aan kan..')
    else:
        print('Dit wapen ken ik eerlijk gezegd niet... maar goed, we gaan verder...')

    time.sleep(delay)
    print()
# Nieuwe schild keuze met if en else
    shield = input('Nu je je wapen hebt moet je jezelf ook nog kunnen verdedigen als je niet meer kan aanvallen, wil je een schild? [ja/nee]')
    if shield == 'nee':
        print('Weet je het zeker? .. Nou goed dan je gaat verder zonder schild')
    print()
# Nieuwe tegenstander keuze met if en tenminste 1 elif
    fight = input('Kijk daar verder op.. hou hem in de gaten want hij gaat jou waarschijnlijk aanpakken. [loop verder/pak hem aan]')
    if fight == 'loop verder' and shield == 'ja':
        print('ik hoor voetstappen jij ook...')
        print('Ineens is het misterieuse persoon daar en maakt een slaande beweging met z\'n zwaard.')
        print('Heb jij even geluk dat jij je schild bij je hebt ;)')
    elif fight == 'loop verder' and shield == 'nee':
        print('ik hoor voetstappen jij ook?...')
        print('Ineens is het misterieuse persoon daar en maakt een slaande beweging met z\'n zwaard.')
    elif fight == 'pak hem aan' and weapon == 'zwaard':
        print('Je loopt op hem af... pakt je zwaard en... ')
    elif fight == 'pak hem aan' and weapon =='bijl':
        print('je loopt op hem af... pakt je bijl en... je raakt het onbekende persoon.')
        print('De bijl was blijkbaar een goede keus!')
    elif fight == 'pak hem aan' and weapon =='mes':
        print('je loopt op hem af... pakt je mes en... je raakt het onbekende persoon.')
        print('Het mes was blijkbaar een goede keus!')

    print()
    
# nieuw einde
    if fight == 'loop verder' and shield == 'nee' or fight == 'pak hem aan' and weapon == 'zwaard' or fight == 'loop verder' and weapon == 'zwaard':
        print('Helaas, je hebt het niet overleeft...')
    else:
        print('Je hebt het overleefd, goed joh!')
        

