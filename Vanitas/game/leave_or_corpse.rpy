default reschedule_kloth = False
default weak_symbiont = False

label leave_or_corpse:
    $ last_try_find_kloth = False
    $ weak_symbiont = True
    "Abhauen oder Leiche betrachten"

    menu:
        "Leiche":
            jump kloth_corpse
        "Abhauen":
            jump leave_and_go_pill

label leave_and_go_pill:
    "Macht sich auf den Weg ins Büro und nimmt die Pille"

    jump pill

label kloth_corpse:
    "Realisation dass es Kloth ist; Mental Breakdown"

    "ERINNERUNG; Kloth spricht Atropos an und bittet um ein Gespräch, wirkt extrem angespannt (Symbiont versucht Atropos davon abzubringen)"

    "Mit Kloth reden?"

    jump conversation_with_kloth

label conversation_with_kloth:
    if reschedule_kloth:
        menu:
            "Annehmen":
                jump accept_conversation_kloth
            "Ablehnen":
                jump refuse_conversation_kloth
    else:
        menu:
            "Annehmen":
                jump accept_conversation_kloth
            "Verschieben":
                jump reschedule_conversation_kloth
            "Ablehnen":
                jump refuse_conversation_kloth

label reschedule_conversation_kloth:
    $ reschedule_kloth = True
    "Kloth drängt auf das Gespräch jetzt gleich, rückkehr zur Auswahl"

    jump conversation_with_kloth

label accept_conversation_kloth:
    "Kloth fängt an über dubiose Sachen über die Firma mit Hint auf das Passwort ~Sadness~"
    "Symbiont mischt sich ein (Glitcheffekte), Atropos bekommt den Rest des Gesprächs nicht mit"
    "Kloth denkt, dass Atropos nun auf seiner Seite ist und bittet ihn darum, ihm zu Helfen"
    "Sequenz: Atropos wird wütend und packt Kloth, Chesis kommt dazu und einer von beiden stößt Kloth die Treppe runter"

    "Was untersuchen?"

    jump selection_kloth_office_after_corpse

label refuse_conversation_kloth:
    "Atropos lehnt ab, weil der Tag heute schon zu stressig war; Kloth wendet sich enttäuscht ab und redet im Hintergrund mit Chesis"
    "Sequenz: Chesis stößt Kloth die Treppe herunter; Rückkehr in die Gegenwart"
    "Atropos wird wütend auf Chesis, wie konnte dieser das ihrem Freund antun?"
    "GEGENWART Realisation: Kloth hatte etwas wichtiges zu sagen; macht sich auf den Weg zu seinem Büro um Hinweise zu suchen"

    "Was untersuchen?"

    jump selection_kloth_office_after_corpse
