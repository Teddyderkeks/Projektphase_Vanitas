default pill_taken = False
default straight_office = False

label start:
    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    scene atropos_falling

    "Will ich versuchen etwas zu ändern?"

    menu:
        "ja":
            jump change
        "nein":
            jump quick_ending

label quick_ending:
    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

label change:
    scene street

    "Timelaps zurück; Atropos ist gerade auf Weg zur Arbeit"
    "Monolog über Aither zur Einführung die Welt"

    "Erinnerung an die Tablette und dass man sie täglich nehmen sollte"
    "Erinnerung dass man das in letzter Zeit nicht regelmäßig gemacht hat"

    "Tablette heute genommen/nehm ich sie jetzt?"

    menu:
        "ja":
            jump take_pill
        "Nein,ich brauch das nicht":
            jump not_take_pill
        "Nein, mach ich aber später":
            jump later_take_pill

label take_pill:
    $ pill_taken = True

    "Monolog: Tablette ist sehr wichtig, Reue die Tablette in letzter Zeit nicht regelmäßig genommen zu haben"

    jump shop

label not_take_pill:
    $ pill_taken = False

    "Monolog: Tablette sowieso überflüssig, ich bin doch auch so glücklich"

    jump shop

label later_take_pill:
    $ pill_taken = False

    "Monolog: Tablette wichtig (mit Erklärung), aber die letzten Tage hab ich auch nix bemerkt"

    jump shop

label shop:
    scene shop

    "Ankunft bei Aither, wird im Verkaufsraum von Kollegen begrüßt"

    "Was tun?"

    menu:
        "Plausch mit Kollegen":
            jump conversation_with_seller
        "Ab zur Arbeit":
            jump work

label conversation_with_seller:
    "Gespräch mit Verkäufer, Informationen über Firma / Anan"

    if pill_taken:
        "Chesis kommt an und grüßt Atropos gut gelaunt"

        scene hall

        "beide machen sich gemeinsam auf den Weg zur Arbeit und erinnern sich an ~früherere Zeiten~ von Atropos"
        "Chesis und Kloth; Anan läuft an ihnen vorbei und grüßt kurz"

        scene laboratory

        "Erreichen des Arbeitsplatzes in guter Stimmung, Plausch mit Kollegen dort"

        jump good_mood

    else:
        "Chesis kommt an und grüßt Atropos gut gelaunt"
        "auf Frage ob er weiß wo Kloth ist gibt er eine kryptische Antwort und muss dann schnell los zur Arbeit"

        jump work

label work:
    if pill_taken:

        scene hall

        "Anan wird gesehen, ignoriert Atropos jedoch bzw grüßt nur kurz"

        scene laboratory

        "Erreichen des Arbeitsplatzes in guter Stimmung, Plausch mit Kollegen dort"

        "Gespräch wird auf Atropos Freunde gelenkt, Erinnerungen an Atropos und Chesis Anfangszeit bei Aither"

        jump good_mood

    else:
        scene hall

        "Begegnung mit Anan, dieser spricht Atropos darauf an, dass er die Pille anscheinend nicht genommen hat und fordert ihn auf nacher in sein Büro zu kommen, nicht besonders gut aufgelegt"

        "Monolog über die Begegnung, während Atropos auf dem Weg zur Arbeit ist; liegt Anan richtig mit dem Rüffel?"

        "Reaktion auf das Gespräch mit Anan"

        menu:
            "Anan hat ja recht":
                jump anan_is_right
            "Wieso ist das denn so wichtig?":
                jump why_important
            "Was erlaubt er sich?":
                jump be_against

label anan_is_right:
    $ straight_office = True

    "Monolog; Anan hat ja recht, positive Seiten und Erfolge von Aither hervorheben"

    scene laboratory

    "Erreichen des Arbeitsplatzes in guter Stimmung, Plausch mit Kollegen; diese bemerken nichts von dem Gespräch mit Anan"

    jump go_office

label why_important:
    $ straight_office = True

    "Monolog; wieso ist es unbedingt nötig die Pille zu nehmen wenn ich auch ohne glücklich bin?"

    scene laboratory

    "Erreichen des Arbeitsplatzes etwas niedergeschlagen; in Plausch mit Kollegen wird das eben geschehene angesprochen; Reaktion der Kollegen ist jedoch verständnisvoll für Anan"

    jump go_office

label be_against:
    $ straight_office = False

    "Monolog: ich lass mir doch nicht vorschreiben was ich zu tun oder zu las"

    scene laboratory

    "Erreichen des Arbeitsplatzes in mieser Stimmung, Atropos versucht Gespräch mit Kollegen zu vermeiden bzw schnell zu beenden; diese wundern sich darüber"

    jump go_office

label go_office:
    if straight_office:

        "ZEITSPRUNG; Atropos realisiert, dass es Zeit ist Anan aufzusuchen"

        jump office

    else:

        "Will ich gehen?"

        menu:
            "ja":
                jump office
            "nein":
                jump no_office

label good_mood:
    "Atropos konzentriert sich jetzt mit voller Freude auf die Arbeit"

    "ZEITSPRUNG; Mittagspause"

    jump pill

label no_office:
    "Zeit verstreicht, Anan bekommt Aufruf über Lautsprecher ins Büro von Anan zu kommen, dieser ist bereits da"

    jump rueffel
