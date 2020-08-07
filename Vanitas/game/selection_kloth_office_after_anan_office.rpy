default kloth_office_after_anan_office = False

label selection_kloth_office_after_anan_office:
    $ kloth_office_after_anan_office = True

    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "Dokument":
                        jump document_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
        else:
            if read_document_kloth:
                menu:
                    "PC":
                        jump computer_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "PC":
                        jump computer_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
        else:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "PC":
                        jump computer_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "Brief":
                        jump letter_kloth
                    "PC":
                        jump computer_kloth
                    "Dokument":
                        jump document_kloth
                    "Kloth suchen":
                        jump search_kloth_in_stairwell
