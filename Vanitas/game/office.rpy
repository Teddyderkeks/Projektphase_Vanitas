default infos_count_anan = 0
default infos_count_kloth = 0
default read_letter_anan = False
default read_document_anan = False
default read_computer_anan = False
default face_anan_in_office = False
default bomb_trigger_choice = False
default last_try_find_kloth = False
default rage_atropos_bomb = False
default straight_anan_office = False

label office:
    scene hall

    "Macht sich auf den Weg, Anan noch nicht da"

    scene anan_office

    "In Büro umsehen?"

    menu:
        "Ja":
            $ straight_anan_office = True
            jump selection_anan_office
        "Nein":
            jump conversation_with_anan

label conversation_with_anan:
    "Anan kommt an, Schelte für Atropos weil er die Pille nicht genommen hat, Aufforderung dies jetzt zu tun"

    "Reaktion auf die Schelte"

    menu:
        "Einsicht":
            jump understanding
        "Sinn der Pille hinterfragen":
            jump questioning
        "Wütend":
            jump rueffel

label understanding:
    scene hall

    "Atropos geht zurück an seinen Arbeitsplatz und nimmt die Pille"

    jump pill

label questioning:
    "Anan erklärt Wichtigkeit der Pille mit üblichen Argumenten"

    "Reaktion darauf?"

    menu:
        "Einsicht":
            jump understanding
        "Unverständnis":
            jump misunderstanding

label misunderstanding:

    "Anan wird wütend, wird jedoch angerufen und muss kurz weg, befiehlt Atropos hier zu warten"

    jump selection_anan_office

label how_many_infos_anan:
    "Wie viele Sachen angesehen?"

    if infos_count_anan == 0:
        if  straight_anan_office:
            scene hall

            "Atropos verlässt das Büro wieder weil ihn Gewissensbisse (Symbiont) plagen, Anan kommt an, Schelte für Atropos weil er die Pille nicht genommen hat, Aufforderung dies jetzt zu tun"

            "Reaktion auf die Schelte"

            menu:
                "Wütend":
                    jump rueffel
                "Einsichtig":
                    jump understanding

        else:
            "Anan kommt zurück, Atropos zeigt Einsicht, Anan fragt nach ob Atropos Kloth gesehen hat und schickt ihn zurück um die Pille zu nehmen"

            jump understanding

    if infos_count_anan == 1 or infos_count_anan == 2:
        if  straight_anan_office:

            scene hall
            "Atropos verlässt das Büro und wartet auf Anan, welcher kurze Zeit später ankommt und anfängt Atropos wegen der nicht genommenen Pille zu rüffeln"

        else:
            "Anan kommt zurück und bemerkt nichts; fragt nach ob Atropos Kloth schon gesehen hat und will ihn zurückschicken um die Pille zu nehmen"

        jump one_or_two_infos

    if infos_count_anan == 3:
        if straight_anan_office:
            "Atropos erhebt sich vom Schreibtisch als Anan in seinem Büro kommt"

        $ last_try_find_kloth = True
        "Anan erwischt Atropos und es kommt zum riesen Streit, Atropos konfrontiert Anan mit den Hinweisen, Anan wirft ihn raus und kündigt den Rauswurf aus der Firma an"

        jump visit_kloth

label one_or_two_infos:
    "Anan mit den Tatsachen konfrontieren?"

    menu:
        "Ja":
            $ last_try_find_kloth = True
            jump face_anan
        "Nein":
            jump not_face_anan

label face_anan:
    $ bomb_trigger_choice = True

    "Riesen Streit, da Atropos in privaten Dokumenten geschnüffelt hat; Anan wirft Atropos raus und kündigt den Rauswurf aus der Firma an"

    jump  visit_kloth

label not_face_anan:
    scene hall

    "Atropos verlässt das Büro; Monolog über Sinn der Firma und Moralischen Aspekt"

    "Firma OK oder böse?"

    menu:
        "OK":
            jump back_to_work
        "Böse":
            $ rage_atropos_bomb = True
            $ face_anan_in_office = True
            $ bomb_trigger_choice = True
            jump visit_kloth

label visit_kloth:
    scene hall
    if face_anan_in_office:
        "Beschließt, Kloth aufzusuchen und ihn dazu zu befragen, da dieser ja Sekretär von Anan ist"

    else:
        "Atropos beschließt Kloth aufzusuchen und ihn nach diesen Sachen zu befragen, da er ja Sekretär von Anan ist"

    "Kloth antwortet nicht auf Anrufe/Nachrichten; Beschluss sein Büro aufzusuchen;"

    scene kloth_office

    "Kloth nicht da, Atropos durchsucht das Büro"

    "Was untersuchen? Oder Kloth suchen?"

    jump selection_kloth_office_after_anan_office

label search_kloth_in_stairwell:
    $ rage_atropos_bomb = False
    scene hall

    "Sucht Kloth,"

    scene stairs_down

    "findet die Leiche im Treppenhaus"

    jump leave_or_corpse

label how_many_infos_kloth:

    "Wie viele Sachen angesehen?"

    if infos_count_kloth == 1 or infos_count_kloth == 2:
        jump choice_bomb

    if infos_count_kloth == 3:
        if last_try_find_kloth:
            jump last_search_kloth
        else:
            jump next_step_with_bomb

label last_search_kloth:
    $ rage_atropos_bomb = True
    "Kloth suchen?"

    menu:
        "Ja":
            jump end_search_kloth
        "Nein, diese Informationen sind genug":
            jump next_step_with_bomb

label end_search_kloth:
    scene hall

    "Sucht Kloth"

    scene stairs_down

    "findet die Leiche im Treppenhaus und erinnert sich dass er ihn selbst gestoßen hat"
    "Kann nicht begreifen, wie ein Produkt, welches Glücklichkeit verspricht so etwas bewirken kann/mit Menschen anstellen kann"

    scene hall
    "Verfällt in Wahnsinn,"
    scene server_room
    "sucht die Bombe auf und stellt den Timer auf 10 Minuten,"
    scene hall
    "geht dann (immer noch dem Wahnsinn verfallen) hinaus und Verbarrikadiert so viele Türen wie möglich"

    scene server_room
    "Kehrt zur Bombe zurück und setzt sich mit irrem Lachen davor und wartet bis sie runterzählt; hört auch klopfen und verwirrte Stimmen vor der Tür"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return
