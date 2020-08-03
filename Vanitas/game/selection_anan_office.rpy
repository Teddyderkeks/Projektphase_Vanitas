label selection_anan_office:

    if read_letter_anan:
        if read_computer_anan:
            if read_document_anan:
                jump how_many_infos
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
