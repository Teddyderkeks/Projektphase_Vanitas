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

label defuse_bomb:
    scene server_room

    "Endsequenz, Atropos versucht die Bombe zu entschärfen, scheitert jedoch, da Kloth einen Failsafe eingebaut hat"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

label trigger_bomb:
    scene server_room

    if secret_ending:
        "Endsequenz, jedoch stark verschwommen, da Symbiont starke Rolle übernimmt"

        "SECRET ENDING: Atropos geht am nächsten Tag zu einer anderen Arbeit, ein paar Tage später Zeitungsbericht über Zerstörung von Aither"

        $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    else:
        "Endsequenz, jedoch stark verschwommen, da Symbiont starke Rolle übernimmt"

        $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")
