label selection_kloth_office:
    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                jump everything_seen
            else:
                menu:
                    "Dokument":
                        jump document_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
        else:
            if read_document_kloth:
                menu:
                    "PC":
                        jump computer_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "PC":
                        jump computer_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
        else:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "PC":
                        jump computer_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "Brief":
                        jump letter_kloth
                    "PC":
                        jump computer_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth

label letter_kloth:
    $ read_letter_kloth = True
    $ infos_count_kloth += 1

    "Liest sich wie eine Art Abschiedsbrief voller Angst und Zweifel über Aither"

    jump selection_kloth_office

label computer_kloth:
    $ read_computer_kloth = True
    $ infos_count_kloth += 1

    "Online Blog über Hinweise auf einen Bombenleger bzw Zerstörer von Aither"

    jump selection_kloth_office

label document_kloth:
    $ read_document_kloth = True
    $ infos_count_kloth += 1

    "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

    jump selection_kloth_office
