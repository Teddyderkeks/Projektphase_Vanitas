label pill:
    scene laboratory

    "Atropos macht sich auf die Suche nach Chesis und Kloth"

    "Wen zuerst suchen/anrufen?"

    menu:
        "Kloth":
            jump search_kloth
        "Chesis":
            jump search_chesis

label search_chesis:
    "Atropos sucht Chesis auf und schlägt vor, Kloth zu suchen, Chesis ist davon nicht besonders begeistert und versucht Atropos zu überzeugen, nicht nach ihm zu suchen"
    "Auf Frage, ob Chesis weiß was mit Kloth los ist gibt dieser eine Kryptische Antwort (sowas wie: das weißt du doch selbst)"

    "Losgehen und Kloth suchen oder Pause mit Chesis verbringen?"

    menu:
        "Kloth":
            jump search_kloth
        "Chesis":
            jump still_search_chesis

label still_search_chesis:
    scene anan_office

    "Gespräch dreht sich über Firma und Vergangenheit"
    "Atropos macht sich wirklich sorgen um Kloth, Chesis versucht ihn zu beruhigen und alles herunterzuspielen"

    "Doch nach Kloth suchen?"

    menu:
        "Ja":
            jump search_kloth
        "Nein":
            jump not_search_kloth

label not_search_kloth:
    if read_document_kloth:
        1.Dialog

    if infos_count_kloth = 1:
        2.Dialog
    if infos_count_kloth = 2:
        2.Dialog

    scene laboratory


    "Atropos geht nach der Pause weiter seiner Arbeit nach"

    "ZEITSPRUNG, ein paar Stunden später"

    scene hall

    "Atropos muss zum Serverraum, sieht Bombe kurz vor Detonation"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return
