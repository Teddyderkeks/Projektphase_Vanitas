default kloth_office_choice = False
default password_right = False

label selection_kloth_office:
    $ kloth_office_choice = True

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

label letter_kloth:
    $ read_letter_kloth = True
    $ infos_count_kloth += 1

    if read_computer_kloth:
        "anderer Dialog"
    else:
        "Liest sich wie eine Art Abschiedsbrief voller Angst und Zweifel über Aither"

    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label computer_kloth:
    $ read_computer_kloth = True
    $ infos_count_kloth += 1

    "Möglichkeit zur Eingabe Passwort"

    python:
        password = renpy.input ("Passwort:")

    if password == "Sadness" or password == "sadness":
        $ password_right = True
        "Dialog"
    else:
        "anderer Dialog"

    "Dialog nach Passwort"

    "Blog wird gezeigt"

    python:
        password = password.strip()
        
    if password_right:
        "Dialog korrektes Passwort"
    else:
        "Dialog inkorrektes Passwort"

    "Dialog nach Blog"

    if infos_count_kloth == 1 or infos_count_kloth == 2:
        "Dialog wenn noch nicht alles gefunden"

    "Dialog"

    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label document_kloth:
    $ read_document_kloth = True
    $ infos_count_kloth += 1

    if read_computer_kloth:
        "anderer Dialog"
    else:
        "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office
