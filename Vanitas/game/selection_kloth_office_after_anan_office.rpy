default kloth_office_after_anan_office = False
default sawshelf = False
default sawpictureskloth = False
default sawworldmap =False

label selection_kloth_office_after_anan_office:
    $ renpy.fix_rollback()
    $ kloth_office_after_anan_office = True
    $ lookaroundklothsoffice = True

    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                $ klothwatchedeverything= True
                $ lookaroundklothsofficewatchedeverything= True
                if safeopen == True:
                    $klotheverythingseensafeopen= True
                else:
                    $klotheverythingseenbutnotsafeopen = True
                jump how_many_infos_kloth
            else:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth

                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump search_kloth_in_stairwell

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth

                    "Ich werde mir das Dokument anschauen.":
                        $ renpy.fix_rollback()
                        jump document_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth

        else:
            if read_document_kloth:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        $ renpy.fix_rollback()
                        jump computer_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth


            else:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde mir das Dokument anschauen.":
                        $ renpy.fix_rollback()
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        $ renpy.fix_rollback()
                        jump computer_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth


    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        $ renpy.fix_rollback()
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth

            else:
                menu:

                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell

                    "Ich werde mir das Dokument anschauen.":
                        $ renpy.fix_rollback()
                        jump document_kloth

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        $ renpy.fix_rollback()
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth


        else:
            if read_document_kloth:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        $ renpy.fix_rollback()
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ renpy.fix_rollback()
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump search_kloth_in_stairwell

                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        $ renpy.fix_rollback()
                        jump pictureskloth_kloth

                    "Ich werde den Computer durchsuchen.":
                        $ renpy.fix_rollback()
                        jump computer_kloth

                    "Ich werde mir den Brief anschauen.":
                        $ renpy.fix_rollback()
                        jump letter_kloth

                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        $ renpy.fix_rollback()
                        jump worldmap_kloth


            else:
                if (sawsafe==True) or (sawpictures==True) or (sawbooks==True):
                    menu:
                        "Ich werde das Regal untersuchen."  if sawshelf == False:
                            $ renpy.fix_rollback()
                            jump shelf_kloth

                        "Ich suche besser nach Kloth.":
                            $ renpy.fix_rollback()
                            # Atropos Gedanken
                            symb"Ich suche besser nach Kloth."
                            # Atropos Gedanken
                            symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                            jump search_kloth_in_stairwell

                        "Ich werde mir das Dokument anschauen.":
                            $ renpy.fix_rollback()
                            jump document_kloth

                        "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                            $ renpy.fix_rollback()
                            jump pictureskloth_kloth

                        "Ich werde den Computer durchsuchen.":
                            $ renpy.fix_rollback()
                            jump computer_kloth

                        "Ich werde mir den Brief anschauen.":
                            $ renpy.fix_rollback()
                            jump letter_kloth
                        "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                            $ renpy.fix_rollback()
                            jump worldmap_kloth
                else:
                    menu:
                        "Ich werde das Regal untersuchen."  if sawshelf == False:
                            $ renpy.fix_rollback()
                            jump shelf_kloth

                        "Nein, ich suche besser nach Kloth.":
                            $ renpy.fix_rollback()
                            # Atropos Gedanken
                            symb"Nein, ich suche besser nach Kloth."
                            # Atropos Gedanken
                            symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                            jump search_kloth_in_stairwell

                        "Ich werde mir das Dokument anschauen.":
                            $ renpy.fix_rollback()
                            jump document_kloth

                        "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                            $ renpy.fix_rollback()
                            jump pictureskloth_kloth

                        "Ich werde den Computer durchsuchen.":
                            $ renpy.fix_rollback()
                            jump computer_kloth

                        "Ich werde mir den Brief anschauen.":
                            $ renpy.fix_rollback()
                            jump letter_kloth
                        "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                            $ renpy.fix_rollback()
                            jump worldmap_kloth
