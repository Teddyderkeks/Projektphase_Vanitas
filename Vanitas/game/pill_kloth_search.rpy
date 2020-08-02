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

    menu:
        "Brief"
        "PC"
        "Dokument"
        "Kloth nicht suchen":
            jump not_search_kloth
        "Kloth"
