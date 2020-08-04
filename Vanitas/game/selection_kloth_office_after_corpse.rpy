label selection_kloth_office_after_corpse:
    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "Dokument":
                        jump document_kloth
                    "Büro verlassen":
                        jump how_many_infos_kloth
        else:
            if read_document_kloth:
                menu:
                    "PC":
                        jump computer_kloth
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "PC":
                        jump computer_kloth
                    "Dokument":
                        jump document_kloth
                    "Büro verlassen":
                        jump how_many_infos_kloth
    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Büro verlassen":
                        jump how_many_infos_kloth
            else:
                menu:
                    "Brief":
                        jump letter_kloth
                    "Dokument":
                        jump document_kloth
                    "Büro verlassen":
                        jump how_many_infos_kloth
        else:
            if read_document_kloth:
                menu:
                    "Brief":
                        jump letter_kloth
                    "PC":
                        jump computer_kloth
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
