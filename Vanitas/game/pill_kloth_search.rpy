default read_letter_kloth = False
default read_computer_kloth = False
default read_document_kloth = False
default secret_ending = False

label search_kloth:
    scene hall

    "Kloth antwortet nicht auf Nachricht/Anruf"
    "Atropos macht sich auf den Weg zu seinem Büro"

    "Auf dem Weg: Gedanken über das Fehlen von Kloth (hat ihn schon seit gestern nicht gesehen)"

    scene kloth_office

    "Kloth nicht in seinem Büro"

    "In Anans Büro nachsehen?"

    menu:
        "Ja":
            jump search_kloth_in_anan_office
        "Nein":
            jump search_kloth_without_anan_office

label search_kloth_in_anan_office:
    scene anan_office

    "Weder Anan noch Kloth anwesend"

    "Versuchen sich im Büro umzusehen?"

    menu:
        "Ja":
            jump symbiont_in_between
        "Nein":
            jump search_kloth_without_anan_office

label symbiont_in_between:
    "Symbiont schaltet sich ein und verhindert dies"

    jump search_kloth_without_anan_office


label search_kloth_without_anan_office:
    scene hall

    "Erinnerung (NEU) an Gespräch mit Kloth, allerdings durch Symbionten verwischt, dieser lässt Kloth als Wahnsinnigen dastehen;"
    "Atropos spricht Kloth darauf an, dass er in letzter Zeit nicht so gut aussieht (Alki)"

    "Atropos überlegt weiter im Büro von Kloth zu suchen oder Kloth selbst zu suchen"

    scene kloth_office

    "Was untersuchen?Oder Kloth weitersuchen?Oder Kloth nicht suchen?"

    jump selection_kloth_office

label letter_kloth:
    $ read_letter_kloth = True

    "Liest sich wie eine Art Abschiedsbrief voller Angst und Zweifel über Aither"

    jump selection_kloth_office

label computer_kloth:
    $ read_computer_kloth = True

    "Online Blog über Hinweise auf einen Bombenleger bzw Zerstörer von Aither"

    jump selection_kloth_office

label document_kloth:
    $ read_document_kloth = True

    "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

    jump selection_kloth_office

label everything_seen:
    "Wenn alles angesehen"

    "Nach Kloth suchen oder Hinweisen nachgehen?"

    menu:
        "Hinweise":
            jump hints
        "Kloth":
            jump still_search_kloth

label hints:
    $ secret_ending = True

    scene hall

    "Monolog über Firma: ist sie so gut oder Böse, wenn sie einen Freund so in Verzweiflung stürzen kann?"
    "Symbiont nimmt starken Einfluss und möchte Bombe entschärfen"

    "Bombe aufsuchen und auslösen oder entschärfen"

    menu:
        "Entschärfen":
            jump defuse_bomb
        "Auslösen":
            jump trigger_bomb

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
