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
