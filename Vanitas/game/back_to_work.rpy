label back_to_work:
    "Monolog über Gespräch mit Anan, Gedanken über Wirksamkeit der Pille"
    "Sieht Plakate über Happiness und betrachtet sie"

    "Zurück ins Labor (Pille nehmen) oder mit Kollegen reden?"
    menu:
        "Pille/Büro":
            jump take_pill_back_work
        "Kollegen":
            jump talk_with_colleagues

label take_pill_back_work:
    "Atropos kehrt ins Büro zurück und nimmt die Pille"

    jump pill

label talk_with_colleagues:
    "Smalltalk über Aither, Kollegen reden ausschließlich positiv und nehmen Kritik gar nicht wahr"
    "Atropos denkt über das vergangene Gespräch nach und macht sich auf den Weg zurück zu seinem Arbeitsplatz"
    "Stößt auf eine Leiche am Fuß der Treppe"

    jump leave_or_corpse
