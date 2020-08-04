label selection_anan_office:

    if read_letter_anan:
        if read_computer_anan:
            if read_document_anan:
                jump how_many_infos_anan
            else:
                menu:
                    "Dokument":
                        jump document_anan
                    "Nichts":
                        jump how_many_infos
        else:
            if read_document_anan:
                menu:
                    "PC":
                        jump computer_anan
                    "Nichts":
                        jump how_many_infos
            else:
                menu:
                    "PC":
                        jump computer_anan
                    "Dokument":
                        jump document_anan
                    "Nichts":
                        jump how_many_infos
    else:
        if read_computer_anan:
            if read_document_anan:
                menu:
                    "Brief":
                        jump letter_anan
                    "Nichts":
                        jump how_many_infos
            else:
                menu:
                    "Brief":
                        jump letter_anan
                    "Dokument":
                        jump document_anan
                    "Nichts":
                        jump how_many_infos
        else:
            if read_document_anan:
                menu:
                    "Brief":
                        jump letter_anan
                    "PC":
                        jump computer_anan
                    "Nichts":
                        jump how_many_infos
            else:

                "Was im Büro ansehen?"
                menu:
                    "Brief":
                        jump letter_anan
                    "PC":
                        jump computer_anan
                    "Dokument":
                        jump document_anan
                    "Nichts":
                        jump how_many_infos

label letter_anan:
    $ read_letter_anan =True
    $ infos_count_anan += 1

    "Informationen über die frühen Tage von Aither und den Aufbau der Strukturen, Wichtigkeit dass jeder Happiness nimmt weil sonst Chaos ausbricht!"

    jump selection_anan_office

label document_anan:
    $ read_document_anan =True
    $ infos_count_anan += 1

    "Nicht einfach zu verstehende Diagramme und co über das menschliche Gehirn/Psychologie/Wirkungsweisen"

    jump selection_anan_office

label computer_anan:
    $ read_computer_anan =True
    $ infos_count_anan += 1

    "Liste von bekannten nicht-Pillennehmer; Atropos als neuester Eintrag mit Notation ihn zu beobachten und gegebenenfalls Maßnahmen zu ergreifen"

    jump selection_anan_office
