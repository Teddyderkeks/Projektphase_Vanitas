label selection_kloth_office:
    if read_letter:
        if read_computer:
            if read_document:
                jump everything_seen
            else:
                menu:
                    "Dokument":
                        jump document
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
        else:
            if read_document:
                menu:
                    "PC":
                        jump computer
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "PC":
                        jump computer
                    "Dokument":
                        jump document
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
    else:
        if read_computer:
            if read_document:
                menu:
                    "Brief":
                        jump letter
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "Brief":
                        jump letter
                    "Dokument":
                        jump document
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
        else:
            if read_document:
                menu:
                    "Brief":
                        jump letter
                    "PC":
                        jump computer
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
            else:
                menu:
                    "Brief":
                        jump letter
                    "PC":
                        jump computer
                    "Dokument":
                        jump document
                    "Kloth":
                        jump still_search_kloth
                    "Kloth nicht suchen":
                        jump not_search_kloth
