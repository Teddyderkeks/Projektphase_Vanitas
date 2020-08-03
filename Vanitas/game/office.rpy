default infos_count = 0
default read_letter_anan = False
default read_document_anan = False
default read_computer_anan = False

label office:
    scene hall

    "Macht sich auf den Weg, Anan noch nicht da"

    scene anan_office

    "In Büro umsehen?"

    menu:
        "Ja":
            jump selection_anan_office
        "Nein":
            jump conversation_with_anan

label conversation_with_anan:
    "Anan kommt an, Schelte für Atropos weil er die Pille nicht genommen hat, Aufforderung dies jetzt zu tun"

    "Reaktion auf die Schelte"

    menu:
        "Einsicht":
            jump understanding
        "Sinn der Pille hinterfragen":
            jump questioning
        #"Wütend":
            #jump rueffel

label understanding:
    scene hall

    "Atropos geht zurück an seinen Arbeitsplatz und nimmt die Pille"

    jump pill

label questioning:
    "Anan erklärt Wichtigkeit der Pille mit üblichen Argumenten"

    "Reaktion darauf?"

    menu:
        "Einsicht":
            jump understanding
        "Unverständnis":
            jump misunderstanding

label misunderstanding:

    "Anan wird wütend, wird jedoch angerufen und muss kurz weg, befiehlt Atropos hier zu warten"

    jump selection_anan_office

label letter_anan:
    $ read_letter_anan =True
    $ infos_count += 1

    "Informationen über die frühen Tage von Aither und den Aufbau der Strukturen, Wichtigkeit dass jeder Happiness nimmt weil sonst Chaos ausbricht!"

    jump selection_anan_office

label document_anan:
    $ read_document_anan =True
    $ infos_count += 1

    "Nicht einfach zu verstehende Diagramme und co über das menschliche Gehirn/Psychologie/Wirkungsweisen"

    jump selection_anan_office

label computer_anan:
    $ read_computer_anan =True
    $ infos_count += 1

    "Liste von bekannten nicht-Pillennehmer; Atropos als neuester Eintrag mit Notation ihn zu beobachten und gegebenenfalls Maßnahmen zu ergreifen"

    jump selection_anan_office

label how_many_infos:
    "Wie viele Sachen angesehen?"

    if infos_count == 0:
        "wla"
    if infos_count == 1:
        "wlaa"
    if infos_count == 2:
        "wlaa"
    if infos_count == 3:
        "wlaaa"
