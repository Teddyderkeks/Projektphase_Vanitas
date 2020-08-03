label still_search_kloth:
    scene hall

    "Trifft auf Anan, dieser sucht ebenfalls nach Kloth"

    scene stairwell

    "Betreten gemeinsam Treppenhaus und finden Kloths Leiche"

    scene hall

    "ERINNERUNG an das Gespräch mit Kloth"

    scene hall

    "Anan scheint etwas zu begreifen, ist enttäuscht aber nicht unglaublich überrascht;"
    "Atropos wird wegen der gleichgültigen Reaktion wütend, Streit mit Anan mit anschließender Entscheidung, Kloths Hinweisen  nachzugehen und Bombe auszulösen"

    "Was genau tun?"

    menu:
        "Bombe einfach hochjagen":
            jump blow_up_bomb
        "Leute retten, aber Gebäude sprengen":
            jump rescue_people_and_blow_up

label blow_up_bomb:
    scene server_room

    "Atropos sucht den Serverraum auf und stellt den Bombentimer auf 3 Sekunden"

    "Bombe geht hoch, Gedanken was für Schaden bei den Leuten entstanden sein könnte; war das wirklich ok?"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

label rescue_people_and_blow_up:
    scene server_room

    "Stellt den Timer auf 20 Minuten und startet ihn, löst anschließend den Feueralarm aus"

    scene street

    "Gespräch mit Kollegen, jeder ist voller Angst um Aither; Atropos realisiert die Tragweite seiner Entscheidung und rennt zurück, um die Bombe zu entschärfen, kommt jedoch zu spät"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return
