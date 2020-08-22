default kloth_office_after_anan_office = False
default sawshelf = False
default sawpictureskloth = False
default sawworldmap =False

label selection_kloth_office_after_anan_office:
    $ kloth_office_after_anan_office = True

    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                jump how_many_infos_kloth
            else:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth

                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump search_kloth_in_stairwell

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth

                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth

        else:
            if read_document_kloth:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth


            else:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth


    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth

            else:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell

                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth


        else:
            if read_document_kloth:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth

                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth

                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth


            else:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        jump shelf_kloth

                    "Nein, ich suche besser nach Kloth.":
                        # Atropos Gedanken
                        symb"Nein, ich suche besser nach Kloth."
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell

                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        jump pictureskloth_kloth

                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth

                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        jump worldmap_kloth
