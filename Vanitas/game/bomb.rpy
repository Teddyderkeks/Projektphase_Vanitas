label choice_bomb:
    scene hall

    "Monolog über Firma: ist sie so gut oder Böse, wenn sie einen Freund so in Verzweiflung stürzen kann?"
    "Symbiont nimmt starken Einfluss und möchte Bombe entschärfen"

    "Bombe aufsuchen und auslösen oder entschärfen"

    if bomb_trigger_choice:
        menu:
            "Entschärfen":
                jump defuse_bomb
            "Auslösen":
                jump next_step_with_bomb
    else:
        menu:
            "Entschärfen":
                jump defuse_bomb
            "Auslösen":
                jump trigger_bomb

label next_step_with_bomb:
    if bomb_trigger_choice:
        "Atropos verfällt in Rage, als er realisiert was Aither alles unternimmt um die Menschen zu kontrollieren, beschließt die Bombe auszulösen"

    "Was genau tun?"

    if bomb_trigger_choice:
        menu:
            "Bombe einfach hochjagen":
                jump blow_up_bomb
            "Leute retten, aber Gebäude sprengen":
                jump rescue_people_and_blow_up
            "Anan locken":
                jump lure_anan
    else:
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

label lure_anan:
    scene server_room

    "Lockt Anan zur Bombe und löst Feueralarm aus; wartet bei Bombe und stellt den Timer auf 3 Sekunden"
    "Tür geht auf und Atropos startet den Timer; Anan und ein Kollege stehen in der Türe"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

label defuse_bomb:
    scene server_room

    "Endsequenz, Atropos versucht die Bombe zu entschärfen, scheitert jedoch, da Kloth einen Failsafe eingebaut hat"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

label trigger_bomb:
    scene server_room

    if secret_ending:
        "Endsequenz, jedoch stark verschwommen, da Symbiont starke Rolle übernimmt"

        "SECRET ENDING: Atropos geht am nächsten Tag zu einer anderen Arbeit, ein paar Tage später Zeitungsbericht über Zerstörung von Aither"

        $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    else:
        "Endsequenz, jedoch stark verschwommen, da Symbiont starke Rolle übernimmt"

        $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")
