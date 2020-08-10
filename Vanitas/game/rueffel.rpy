label rueffel:
    scene anan_office

    "Anan gibt einen Einlauf, weil Atropos die Pille nicht genommen hat + schlechtes Benehmen"

    "Reaktion?"

    menu:
        "Einsichtig":
            jump back_to_work
        "Wütend/Agressiv":
            jump expulsion_office

label expulsion_office:
    scene hall

    "Anan wirft Atropos aus dem Büro und droht mit Kündigung, wenn er die Pille nicht sofort nimmt"

    "Atropos verlässt das Büro wütend und läuft Chesis über den Weg, dieser ist bemerkenswert gleichgültig/steht auf Anans Seite"

    scene lab

    "ZEITSPRUNG nachdem Atropos ins Labor zurück ist"

    scene hall

    "Anan ruft Atropos nochmal zu seinem Büro für die schrifltiche Kündigung, auf dem Weg dahin machts BOOM"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return
